"""
Copyright (c) 2021 Guilherme Taborda Ribas All rights reserved.

Copyright (c) 2012-2013 Matplotlib Development Team; All Rights Reserved.

Copyright (c) 2017 NumPy developers.

Copyright (c) 2021, Israel Dryer. Revision b35a9984 .

Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team All rights reserved.

Copyright (c) 2001-2002 Enthought, Inc.  2003-2019, SciPy Developers. All rights reserved.

Copyright (c) 2017-2019 Ran Aroussi yfinance - market data downloader https://github.com/ranaroussi/yfinance

Copyright (c) 2012-2021, Michael L. Waskom All rights reserved.

Copyright (c) 2010-2021 by Alex Clark and contributors


This file is part of SclabMoneyMapBacktesting.

    SclabMoneyMapBacktesting is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any later version.

    SclabMoneyMapBacktesting is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with SclabMoneyMapBacktesting.  If not, see <http://www.gnu.org/licenses/>.

"""

import re
import pandas as pd

from Functions import *
from variables import all_signals

def get_prices(data):
	# data = paper, period, timeframe
	if len(data)==3:
		import yfinance as yf

		paper = yf.Ticker(data[0])
		df = paper.history(period=data[1], interval=data[2])

		# Round by paper info, because it was generatin error. yfinance doenst get alwys the same values
		if 'currentPrice' in paper.info.keys():
			rnd = len(str(paper.info['currentPrice']).split('.')[1])
			df = df.round(rnd)

		# Delete lines with NAn values
		df.dropna(inplace=True)
		df.reset_index(inplace=True)
		df.rename(columns={'index':'Date','Datetime':'Date'}, inplace=True)

		df['Date'] = pd.to_datetime(df['Date'])
		df.sort_values(by='Date', inplace=True)

		return df
	else:
		# data = file, codec, delimeter, date
		df = pd.read_csv(data[0], encoding=data[1].lower(), sep=data[2].replace('"', '')).iloc[:,:6]#, data[3])
		df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']

		# Delete lines with NAn values
		df.dropna(inplace=True)
		df.reset_index(drop=True, inplace=True)

		df['Date'] = pd.to_datetime(df['Date'])
		df.sort_values(by='Date', inplace=True)

		return df

def calculate_setups(data, enter, quit):
	df = get_prices(data)

	enter_query = ''		
	for q in enter.split(' '):
		if q:
			if q=='[':
				enter_query += '('
			elif q==']':
				enter_query += ')'
			elif q=='&':
				enter_query += '&'
			elif q=='|':
				enter_query += '|'
			else:
				par = re.search(r'\((.*?)\)',q).group(1)
				func = q.replace('('+par+')', '')
				if func in all_signals:
					# Calculate functions
					functions_dict[func](df, par)
				enter_query+=' (`'+func+'('+par+')`) '

	quit_query = ''		
	for q in quit.split(' '):
		if q:
			if q=='[':
				quit_query += '('
			elif q==']':
				quit_query += ')'
			elif q=='&':
				quit_query += '&'
			elif q=='|':
				quit_query += '|'
			else:
				par = re.search(r'\((.*?)\)',q).group(1)
				func = q.replace('('+par+')', '')
				if func in all_signals:
					# Calculate functions	
					functions_dict[func](df, par)
				quit_query+=' (`'+func+'('+par+')`) '

	df['Entrada_Compra'] = df.eval(enter_query)
	df['Saida_Compra'] = df.eval(quit_query)

	# # In future, in case different startegies for buy and sell could be applied
	df['Entrada_Venda'] = df['Saida_Compra']
	df['Saida_Venda'] = df['Entrada_Compra']	

	
	return df
	
def backtesting(data, enter, quit, longOp, shortOp, daytradeOp, quantity, fees, entry_price, entry_day, quit_price, quit_day):
	df = calculate_setups(data, enter, quit)

	df['Date'] = pd.to_datetime(df['Date'])

	preco_entrada = []
	preco_saida = []
	data_entrada = []
	data_saida = []
	tipo_op = []

	dia_listaIN = []
	dia_listaOUT = []

	total_dias = len(df.index)

	dia = df.index[0]
	pos_aberta = False

	while dia < total_dias - entry_day:
		# Test for long strategy
		if (df.loc[dia, 'Entrada_Compra']) and longOp:
			tipo_op.append('Comprada')
			dia_listaIN.append(dia)
			dia = dia + entry_day
			data_entrada.append(df.loc[dia,'Date'])
			preco_entrada.append(-df.loc[dia, entry_price])
			pos_aberta = True

			while dia < total_dias - quit_day: # se não tiver dias suficientes tem que sair
				if daytradeOp:
					if data_entrada[-1].date() != df.loc[dia,'Date'].date():
						dia_listaOUT.append(dia)
						# dia = dia + quit_day
						data_saida.append(df.loc[dia,'Date'])
						preco_saida.append(df.loc[dia, quit_price])

						pos_aberta = False
						break

				if df.loc[dia, 'Saida_Compra']:
					dia_listaOUT.append(dia)
					dia = dia + quit_day
					data_saida.append(df.loc[dia,'Date'])
					preco_saida.append(df.loc[dia, quit_price])

					pos_aberta = False
					break
				dia = dia + 1
		# Test for short strategy
		elif (df.loc[dia, 'Entrada_Venda']) and shortOp:
			tipo_op.append('Vendida')
			dia_listaIN.append(dia)
			dia = dia + entry_day
			data_entrada.append(df.loc[dia,'Date'])
			preco_entrada.append(df.loc[dia, entry_price])
			pos_aberta = True

			while dia < total_dias - quit_day: # se não tiver dias suficientes tem que sair
				if daytradeOp:
					if data_entrada[-1].date() != df.loc[dia,'Date'].date():
						dia_listaOUT.append(dia)
						# dia = dia + quit_day
						data_saida.append(df.loc[dia,'Date'])
						preco_saida.append(-df.loc[dia, quit_price])

						pos_aberta = False
						break

				if df.loc[dia, 'Saida_Venda']:
					dia_listaOUT.append(dia)
					dia = dia + quit_day
					data_saida.append(df.loc[dia,'Date'])
					preco_saida.append(-df.loc[dia, quit_price])

					pos_aberta = False
					break
				dia = dia + 1
		else:
			dia = dia + 1

	if pos_aberta:
		data_entrada = data_entrada[:-1]
		tipo_op = tipo_op[:-1]
		preco_entrada = preco_entrada[:-1]

	return pd.DataFrame( data={'Data Entrada':data_entrada, 'Data Saida':data_saida, 'Tipo':tipo_op, 'Quantidade':[quantity for q in tipo_op],
								'Custos':[fees for q in tipo_op],'Preco Entrada':preco_entrada, 'Preco Saida':preco_saida}), df

def report(result, df):

	result.loc[:, 'Variacao'] = result['Quantidade']*(result['Preco Entrada']+result['Preco Saida']) - (2*result['Custos'])

	cond1 = [(result['Tipo']=='Comprada'), (result['Tipo']=='Vendida')]
	esc1 = [100*( (result['Preco Saida'].abs()-result['Custos']) - (result['Preco Entrada'].abs()+result['Custos']) ) / ( result['Preco Entrada'].abs()+result['Custos'] ), 
	100*( (result['Preco Entrada'].abs()-result['Custos']) - (result['Preco Saida'].abs()+result['Custos']) ) / ( result['Preco Entrada'].abs()-result['Custos'])]

	result['Variacao(%)'] = np.select(cond1, esc1, default=None)

	cond2 = [result['Variacao']>0, result['Variacao']<0]
	esc2 = ['Lucro', 'Prejuizo']

	result['L/P'] = np.select(cond2, esc2, default='Neutro')

	report_dict = {}	

	# Fazer testes de existencia de colunas Lucro, Prejuizo, Neutro
	total = result.groupby('L/P')['Variacao'].sum()
	qnt = result.groupby('L/P').size()
	med = result.groupby('L/P')['Variacao'].mean()
	med_percentual = result.groupby('L/P')['Variacao(%)'].mean()

	report_dict['total_op'] = len(result.index)

	if 'Lucro' in total.index:
		report_dict['lucro_liq'] = round(total['Lucro'], 2)
	else:
		report_dict['lucro_liq'] = 0

	if 'Prejuizo' in total.index:
		report_dict['prejuizo_liq'] = round(total['Prejuizo'], 2)
	else:
		report_dict['prejuizo_liq'] = 0

	if 'Lucro' in qnt.index:
		report_dict['qnt_lucro'] = qnt['Lucro']
	else:
		report_dict['qnt_lucro'] = 0

	if 'Prejuizo' in qnt.index:
		report_dict['qnt_prejuizo'] = qnt['Prejuizo']
	else:
		report_dict['qnt_prejuizo'] = 0

	if 'Neutro' in qnt.index:
		report_dict['qnt_neutro'] = qnt['Neutro']
	else:
		report_dict['qnt_neutro'] = 0

	if len(result.index) == 0:
		report_dict['percentual_lucro'] = 0
	else:
		report_dict['percentual_lucro'] = round(report_dict['qnt_lucro']/len(result.index), 2)

	if report_dict['prejuizo_liq'] == 0:
		report_dict['fator_lucro'] = 0
	else:		
		report_dict['fator_lucro'] = round(report_dict['lucro_liq']/report_dict['prejuizo_liq'], 2)

	report_dict['ganho_maximo'] = round(result['Variacao'].max(), 2)
	report_dict['ganho_maximo(%)'] = round(result['Variacao(%)'].max(), 2)
	report_dict['perda_maxima'] = round(result['Variacao'].min(), 2)
	report_dict['perda_maxima(%)'] = round(result['Variacao(%)'].min(), 2)

	if 'Lucro' in med.index:
		report_dict['media_ganhos'] = round(med['Lucro'], 2)
	else:
		report_dict['media_ganhos'] = 0

	if 'Prejuizo' in med.index:
		report_dict['media_perdas'] = round(med['Prejuizo'], 2)
	else:
		report_dict['media_perdas'] = 0

	if 'Lucro' in med_percentual.index:
		report_dict['media_ganhos(%)'] = round(med_percentual['Lucro'], 2)
	else:
		report_dict['media_ganhos(%)'] = 0

	if 'Prejuizo' in med_percentual.index:
		report_dict['media_perdas(%)'] = round(med_percentual['Prejuizo'], 2)
	else:
		report_dict['media_perdas(%)'] = 0

	if report_dict['media_perdas'] == 0:
		report_dict['ganhos_por_perdas'] = 0
	else:
		report_dict['ganhos_por_perdas'] = abs(round(report_dict['media_ganhos'] / report_dict['media_perdas'], 2))

	report_dict['retorno'] = round( (report_dict['qnt_lucro']*report_dict['media_ganhos']) + (report_dict['qnt_prejuizo']*report_dict['media_perdas']), 2)
	report_dict['retorno(%)'] = round( (report_dict['qnt_lucro']*report_dict['media_ganhos(%)']) + (report_dict['qnt_prejuizo']*report_dict['media_perdas(%)']), 2)


	result['evolucao_saldo'] = result['Variacao'].cumsum()
	result['evolucao_saldo_max'] = result['evolucao_saldo'].cummax()
	result['drawdowns'] = result['evolucao_saldo_max'] - result['evolucao_saldo']

	report_dict['drawdown_max'] = result['drawdowns'].max()

	if report_dict['drawdown_max'] == 0:
		report_dict['retorno_percentual'] = 0
	else:
		report_dict['retorno_percentual'] = round( 100*report_dict['retorno']/report_dict['drawdown_max'], 2 )

	report_dict['drawdown_max'] = round(report_dict['drawdown_max'], 2)

	fimDD = result['drawdowns'].idxmax()
	inicioDD = result['evolucao_saldo'].iloc[:fimDD].idxmax()

	report_dict['saldo_inicioDD'] = result['evolucao_saldo'].iloc[inicioDD]
	report_dict['saldo_fimDD'] = result['evolucao_saldo'].iloc[fimDD]

	report_dict['inicio_drawdown'] = result['Data Entrada'].iloc[inicioDD]
	report_dict['fim_drawdown'] = result['Data Entrada'].iloc[fimDD]


	report_dict['df_report'] = result
	report_dict['df_cotation'] = df

	return report_dict

