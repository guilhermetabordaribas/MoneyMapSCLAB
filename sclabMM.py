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

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from ttkbootstrap import Style
import webbrowser

from PIL import ImageTk, Image

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import numpy as np
import seaborn as sns
from pandas import DataFrame

import variables as my_vars
import Report as report


root = Tk()
root.title("SCLAB - MoneyMap (www.sclab.com.br)")
img = ImageTk.PhotoImage(file='img/sclab-logo-icon.ico')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("1100x600")
style = Style(theme='darkly')

pady = 5
padx = 10

result_report = {}

def FrameWidth(event):
	canvas_width = event.width
	cotation_canvas.itemconfig(cf, width=canvas_width-10)
	cotation_canvas.configure(scrollregion=cotation_canvas.bbox("all"))

	result_canvas.itemconfig(rf, width=canvas_width-10)
	result_canvas.configure(scrollregion=result_canvas.bbox("all"))

	about_canvas.itemconfig(af, width=canvas_width-10)
	about_canvas.configure(scrollregion=about_canvas.bbox("all"))

# Tenha preencher codec e sep automaticamente
def descobre_codec_separador(file):
	for i,codec in enumerate(my_vars.codec):
		try:
			with open(file, mode='r', encoding=codec) as in_file:
				in_file.readline()
			pass
		except:
			erro_codec = True			
			pass
		else:
			erro_codec = False
			combobox_codec.current(i)
			break

	if erro_codec:
		message = 'Por favor, corrija o(s) erro(s) encontrados abaixo:\n\n'
		message += '\u2022 Não conseguimos identificar o Codec automticamente, por favor, insira manualmente.\n\n'
		messagebox.showwarning(title='ERROS ENCONTRADOS!!!', message=message)

	erro_sep = True
	for i,sep in enumerate(my_vars.delimiter):
		with open(file, mode='r', encoding=codec) as in_file:
			if len(in_file.readline().split(sep.replace('"', ''))) >= 5:
				combobox_delimiter.current(i)
				erro_sep = False			
				break
	
	if erro_sep:
		message = 'Por favor, corrija o(s) erro(s) encontrados abaixo:\n\n'
		message += '\u2022 Não conseguimos identificar o Delimitador automticamente, por favor, insira manualmente.\n\n'
		messagebox.showwarning(title='ERROS ENCONTRADOS!!!', message=message)


def open_file():
	filename = filedialog.askopenfilename()
	entry_filePath.config(state='normal')
	entry_filePath.delete(0, 'end')
	entry_filePath.insert('end', filename)
	entry_filePath.config(state='readonly')

	descobre_codec_separador(filename)
	return filename

def save_cotation_file():
	file_name = filedialog.asksaveasfilename(defaultextension='.csv', title='Save Cotation File')#, initialdir='/' filetypes=(('Text Files','*,txt')), 
	if file_name:
		if 'df_cotation' in result_report.keys():
			result_report['df_cotation'].to_csv(file_name, index=False)

def save_backtesting_file():
	file_name = filedialog.asksaveasfilename(defaultextension='.csv', title='Save Backtesting File')# initialdir='/', filetypes=(('Text Files','*,txt')), 
	if file_name:
		if 'df_report' in result_report.keys():
			result_report['df_report'].to_csv(file_name, index=False)

def save_basic_report_file():
	file_name = filedialog.asksaveasfilename(defaultextension='.csv', title='Save Basic Report File')# initialdir='/', filetypes=(('Text Files','*,txt')), 
	if file_name:
		if 'df_report' in result_report.keys():
			with open(file_name, 'w') as in_file:
				txt = \
"""Total de operações:;{}
Total de trades vencedores:;{}
Total de trades perdedores:;{}
Total de lucro líquido:;${}
Total de perda líquida:;${}
Percentual lucrativo:;{}
Fator de lucro:;{}
Ganho máximo:;${}({}%)
Média de ganhos:;${}({}%)
Perda máxima:;${}({}%)
Média de perdas:;${}({}%)
Razão ganhos/perdas:;{}
Retorno médio:;${}
Máximo Drawdown:;$-{}
Retorno Percentual:;{}%""".format(
	# data[0], data[1], data[2],
	result_report['total_op'],
	result_report['lucro_liq'],result_report['qnt_lucro'],
	result_report['prejuizo_liq'],result_report['qnt_prejuizo'],
	result_report['percentual_lucro'],
	result_report['fator_lucro'],
	result_report['ganho_maximo'],result_report['ganho_maximo(%)'],
	result_report['perda_maxima'],result_report['perda_maxima(%)'],
	result_report['media_ganhos'],result_report['media_ganhos(%)'],
	result_report['media_perdas'],result_report['media_perdas(%)'],
	result_report['ganhos_por_perdas'],
	result_report['retorno'],
	result_report['drawdown_max'],
	# result_report['inicio_drawdown'],
	# result_report['fim_drawdown'],
	result_report['retorno_percentual']
	)

				in_file.write(txt)

def open_book_site(e):
	webbrowser.open_new('https://www.sclab.com.br/sclab-finc/TutorialPythonBook/')

def change_source_prices(e):
	if combobox_select_source.get() == 'Cotação Yahoo-finance':
		label_instructions['text'] = 'As cotações possuem os mesmos símbolos do site Yahoo Finance. Após escolher o ativo, deve-se definir o período e o intervalo.\nÉ importante lembrar que os valores tipo "NAN" são deletados, nenhum outro tratamento é feito sobre os dados do Yahoo Finance.'		

		# Must be showed
		combobox_select_paper.grid(row=3, column=0, pady=pady, padx=padx, sticky='nsew')
		combobox_select_period.grid(row=3, column=1, pady=pady, padx=padx, sticky='nsew')
		combobox_select_timeframe.grid(row=3, column=2, pady=pady, padx=padx, sticky='nsew')

		# Must be hidden
		# checkbutton_intraday.grid_forget()
		button_openFile.grid_forget()
		entry_filePath.grid_forget()
		combobox_codec.grid_forget()
		combobox_delimiter.grid_forget()
		combobox_date_fmt.grid_forget()
	else:
		label_instructions['text'] = 'A disposição das colunas de dados deve ser: Data | Abertura | Máxima | Mínima | Fechamento | Volume\nO separador decimal deve ser o ponto "."'

		# Must be showed
		# checkbutton_intraday.grid(row=1, column=0, pady=pady, padx=padx,sticky='nsew')
		button_openFile.grid(row=3, column=0, pady=pady, padx=padx,sticky='nsew')
		entry_filePath.grid(row=3, column=1, columnspan=2, pady=pady, padx=padx, sticky='nsew')
		combobox_codec.grid(row=4, column=0, pady=pady, padx=padx,sticky='nsew')
		combobox_delimiter.grid(row=4, column=1, pady=pady, padx=padx, sticky='nsew')
		combobox_date_fmt.grid(row=4, column=2, pady=pady, padx=padx, sticky='nsew')		

		# Must be hidden
		combobox_select_paper.grid_forget()
		combobox_select_period.grid_forget()
		combobox_select_timeframe.grid_forget()


def change_timeframe(e):
	# Alguns timeframes não estão disponíveis para determinados períodos
	if combobox_select_period.get() in ['1d']:
		combobox_select_timeframe['values'] = [t for t in my_vars.timeframe if t not in ['1wk','1mo','3mo'] ]
		combobox_select_timeframe.current(0)

	elif combobox_select_period.get() in ['5d']:
		combobox_select_timeframe['values'] = [t for t in my_vars.timeframe if t not in ['1wk','1mo','3mo','5d'] ]
		combobox_select_timeframe.current(0)

	elif combobox_select_period.get() in ['1wk']:
		combobox_select_timeframe['values'] = [t for t in my_vars.timeframe if t not in ['1wk','1mo','3mo','5d'] ]
		combobox_select_timeframe.current(0)

	elif combobox_select_period.get() in ['1mo']:
		combobox_select_timeframe['values'] = [t for t in my_vars.timeframe if t not in ['1m','1mo','3mo'] ]
		combobox_select_timeframe.current(0)

	elif combobox_select_period.get() in ['3mo']:
		combobox_select_timeframe['values'] = [t for t in my_vars.timeframe if t not in ['1m','2m','5m','15m', '30m','60m','90m','1h','3mo'] ]
		combobox_select_timeframe.current(0)

	else:
		combobox_select_timeframe['values'] = [t for t in my_vars.timeframe if t not in ['1m','2m','5m','15m', '30m','60m','90m','1h'] ]
		combobox_select_timeframe.current(0)


# Informa sobre erros
def avisa_erros():
	erros = []
	if combobox_select_source.get()=='Cotação Yahoo-finance':
		if combobox_select_paper.get() == 'Escolha o ativo':			
			erros.append('Escolha o ativo/papel a ser usado para o backtesting.')
		if combobox_select_period.get() == 'Escolha o período do histórico':
			erros.append('Você deve escolher o período do histórico das cotações.')
		if combobox_select_timeframe.get() == 'Escolha o timeframe':
			erros.append('Você deve definir o timeframe.')
	else:
		if entry_filePath.get() == '':
			erros.append('Você deve selecionar um arquivo de cotações válido.')
		if combobox_codec.get() == 'Codecs':
			erros.append('Você deve definir o codec de seu arquivo.')
		if combobox_delimiter.get() == 'Delimitador':
			erros.append('Você deve definir o delimitador de dados do arquivo.')
		if combobox_delimiter.get() == 'Formato da Data':
			erros.append('Você deve definir o formato da data das cotações.')

	try:
		float(spinbox_contract_fee.get())
	except:
		erros.append('O custo por operação deve ser um valor numérico.')

	if text_enter_setup.get("1.0",END).replace('\n','').replace(' ','') == '':
		erros.append('Você deve escolher ao menos um estudo para o setup de entrada.')

	if text_quit_setup.get("1.0",END).replace('\n','').replace(' ','') == '':
		erros.append('Você deve escolher ao menos um estudo para o setup de saída.')

	return erros


# Botão que gera o relatório
def gera_calcula_backtest(e):

	# Teste erros
	lista_erros = avisa_erros()
	if lista_erros:
		message = 'Por favor, corrija o(s) erro(s) encontrados abaixo:\n\n'
		for m in lista_erros:
			message += '\u2022 '+m+'\n\n'
		messagebox.showwarning(title='ERROS ENCONTRADOS!!!', message=message)
		return

	# Get data from different sources
	if combobox_select_source.get()=='Cotação Yahoo-finance':		
		data = [combobox_select_paper.get(), combobox_select_period.get(), combobox_select_timeframe.get()]
	else:
		data = [entry_filePath.get(), combobox_codec.get(), combobox_delimiter.get(), combobox_date_fmt.get()]

	# First take off all blanks spaces, and then insert to have control.
	enter = ''
	for s in text_enter_setup.get("1.0",END).replace('\n','').replace(' ',''):
		if s=='[':
			enter += ' [ '
		elif s==']':
			enter += ' ] '
		elif s=='&':
			enter += ' & '
		elif s=='|':
			enter += ' | '
		else:
			enter += s

	quit = ''
	for s in text_quit_setup.get("1.0",END).replace('\n','').replace(' ',''):
		if s=='[':
			quit += ' [ '
		elif s==']':
			quit += ' ] '
		elif s=='&':
			quit += ' & '
		elif s=='|':
			quit += ' | '
		else:
			quit += s


	# Define type of operations short long
	longOp, shortOp = False, False
	if 'Comprado' in combobox_op_type.get():
		longOp = True

	if ('Vendido' in combobox_op_type.get()) or ('vendido' in combobox_op_type.get()):
		shortOp = True

	# Check if is daytrade operation or not
	daytradeOp = False
	if (combobox_op_validate.get() == 'DayTrade'):
		daytradeOp = True

	quantity = int(spinbox_contract_size.get())

	fees = float(spinbox_contract_fee.get())

	entry_price = ''
	if 'abertura' in combobox_op_enterprice.get():
		entry_price = 'Open'
	elif 'fechamento' in combobox_op_enterprice.get():
		entry_price = 'Close'
	elif 'máxima' in combobox_op_enterprice.get():
		entry_price = 'High'
	elif 'mínima' in combobox_op_enterprice.get():
		entry_price = 'Low'

	entry_day = int(spinbox_op_enterday.get())

	quit_price = ''
	if 'abertura' in combobox_op_quitprice.get():
		quit_price = 'Open'
	elif 'fechamento' in combobox_op_quitprice.get():
		quit_price = 'Close'
	elif 'máxima' in combobox_op_quitprice.get():
		quit_price = 'High'
	elif 'mínima' in combobox_op_quitprice.get():
		quit_price = 'Low'

	quit_day = int(spinbox_op_quitday.get())

	root.config(cursor='watch')

	try:
		r, c = report.backtesting(data, enter, quit, longOp, shortOp, daytradeOp, quantity, fees, entry_price, entry_day, quit_price, quit_day)
	except Exception as err:
		message = 'Algo deu errado ao gerar o backtest, por favor, verifique seu arquivo ou tente mudar sua estratégia. O(s) seguinte(s) erro(s) foram encontrados abaixo:\n\n'
		message += '\u2022 '+str(err)+'\n\n'
		messagebox.showwarning(title='ERROS ENCONTRADOS!!!', message=message)
		return
	
	global result_report
	
	try:
		result_report = report.report(r, c)
	except Exception as err:
		message = 'Algo deu errado ao gerar o relatório, por favor, verifique seu arquivo ou tente mudar sua estratégia. O(s) seguinte(s) erro(s) foram encontrados abaixo:\n\n'
		message += '\u2022 '+str(err)+'\n\n'
		messagebox.showwarning(title='ERROS ENCONTRADOS!!!', message=message)
		return

	if result_report['retorno'] <= 0:
		panel.configure(image=img_notstonks)
		panel.image = img_notstonks
	else:
		panel.configure(image=img_stonks)
		panel.image = img_stonks

	
	label_report['text'] = \
"""Dados das cotações:\t{} {} {}

Total de operações:\t{}
Total de trades vencedores:\t{}
Total de lucro líquido:\t${}
Total de trades perdedores:\t{}
Total de perda líquida:\t${}
Percentual lucrativo:\t{}
Fator de lucro:\t\t{}
Ganho máximo:\t\t${}({}%)
Média de ganhos:\t\t${}({}%)
Perda máxima:\t\t${}({}%)
Média de perdas:\t\t${}({}%)

Razão ganhos/perdas:\t{}
Retorno médio:\t\t${}

Máximo Drawdown:\t$-{}
Retorno Percentual:\t{}%""".format(
	data[0], data[1], data[2],
	result_report['total_op'],
	result_report['qnt_lucro'],result_report['lucro_liq'],
	result_report['qnt_prejuizo'],result_report['prejuizo_liq'],
	result_report['percentual_lucro'],
	result_report['fator_lucro'],
	result_report['ganho_maximo'],result_report['ganho_maximo(%)'],
	result_report['perda_maxima'],result_report['perda_maxima(%)'],
	result_report['media_ganhos'],result_report['media_ganhos(%)'],
	result_report['media_perdas'],result_report['media_perdas(%)'],
	result_report['ganhos_por_perdas'],
	result_report['retorno'],
	result_report['drawdown_max'],
	# result_report['inicio_drawdown'],
	# result_report['fim_drawdown'],
	result_report['retorno_percentual']
	)


	# Seleciona a aba resultados automaticamente
	my_notebook.select(1)
	

	# Generate plots	

	df_report = result_report['df_report']

	# Deve-se limpar o plot antes de atualizar os valores
	ax_pizza.clear()
	ax_linha.clear()
	ax_barra.clear()
	ax_histograma.clear()
	ax_scatter.clear()
	ax_linha.clear()
	ax_hora.clear()
	ax_semana.clear()
	ax_mes.clear()

	canvas.draw()

	ax_pizza.set_title('Percentual de Operações de Lucro, Prejuízo e Neutras (%)')
	sizes = [result_report['qnt_lucro'] , result_report['qnt_prejuizo'] , result_report['qnt_neutro']]
	labels = 'Lucro ', 'Prejuízo ', 'Constante '
	ax_pizza.pie(sizes , labels=labels , autopct='%1.2f%%',
		colors=['#6DC75E','#D6675A','#5CA8DA'],
		textprops={'fontsize': 12})

	ax_barra.set_title('Média de Saldos Positivos e Negativos ($)')
	sns.barplot(data=df_report , x='L/P', y='Variacao',
		order=['Lucro', 'Prejuizo', 'Neutro'],
		palette=['#6DC75E','#D6675A','#5CA8DA'],
		ax=ax_barra)

	ax_histograma.set_title('Distribuição de Saldos ($)')
	sns.histplot(df_report['Variacao'], kde=True, stat='probability', ax=ax_histograma)

	ax_scatter.set_title('Scatter de Saldos ($)')
	df_report.plot(x='Data Entrada', y='Variacao',kind='scatter',
		ax=ax_scatter , alpha=.7, s=10)
	ax_scatter.tick_params(axis='x', labelrotation=30)
	# sns.regplot(x='Data Entrada', y='Variacao', ax=ax_scatter, data=data.astype(float))#, alpha=.7, s=10)

	ax_linha.set_title('Evolução do Saldo e MDD ($)')
	df_report.plot(x='Data Entrada', y='evolucao_saldo',
		label='Saldo', ax=ax_linha)

	ax_linha.plot([ result_report['inicio_drawdown'] , result_report['fim_drawdown']], [result_report['saldo_inicioDD'] , result_report['saldo_fimDD']],
		marker='o', linestyle='--', color='purple', label='MDD')	

	h, l = ax_linha.get_legend_handles_labels()
	ax_linha.legend(h, l)
	

	# data.plot(x='Data Entrada', y='drawdowns',
	# 	label='Drawdowns', ax=ax_linha , linewidth=.8)

	# data.plot(x='Data Entrada', y='evolucao_saldo_max',label='Max Acumulado', ax=ax_linha)

	# HORA
	aux = df_report.groupby(by=df_report['Data Entrada'].dt.hour).mean()

	cond = [(aux['Variacao']>=0.0), (aux['Variacao']<0.0)]
	esc = ['Alta', 'Baixa']
	aux['Cor'] = np.select(cond , esc , default=None)

	order = aux.index.sort_values().unique().values

	ax_hora.set_title('Saldo Médio por Hora ($)')

	if len(aux[aux['Variacao']>0].Variacao) > 0:
		sns.barplot(x=aux[aux['Variacao']>0].index , y='Variacao',data=aux[aux['Variacao']>0], order=order ,color='#6DC75E', ax=ax_hora)

	if len(aux[aux['Variacao']<0].Variacao) > 0:
		sns.barplot(x=aux[aux['Variacao']<0].index , y='Variacao',data=aux[aux['Variacao']<0], order=order ,color='#D6675A', ax=ax_hora)

	# Dia da Semana
	aux = df_report.groupby(by=df_report['Data Entrada'].dt.day_name()).mean()

	cond = [(aux['Variacao']>=0.0), (aux['Variacao']<0.0)]
	esc = ['Alta', 'Baixa']
	aux['Cor'] = np.select(cond , esc , default=None)

	order = ['Monday', 'Tuesday','Wednesday', 'Thursday','Friday']

	ax_semana.set_title('Saldo Médio por Dia ($)')
	if len(aux[aux['Variacao']>0].Variacao) > 0:
		sns.barplot(x=aux[aux['Variacao']>0].index , y='Variacao',data=aux[aux['Variacao']>0], order=order ,color='#6DC75E', ax=ax_semana)

	if len(aux[aux['Variacao']<0].Variacao) > 0:
		sns.barplot(x=aux[aux['Variacao']<0].index , y='Variacao',data=aux[aux['Variacao']<0], order=order ,color='#D6675A', ax=ax_semana)

	# Mês
	aux = df_report.groupby(by=df_report['Data Entrada'].dt.month_name()).mean()

	cond = [(aux['Variacao']>=0.0), (aux['Variacao']<0.0)]
	esc = ['Alta', 'Baixa']
	aux['Cor'] = np.select(cond , esc , default=None)

	order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

	ax_mes.set_title('Saldo Médio por Mês ($)')
	if len(aux[aux['Variacao']>0].Variacao) > 0:
		sns.barplot(x=aux[aux['Variacao']>0].index , y='Variacao',data=aux[aux['Variacao']>0], order=order ,color='#6DC75E', ax=ax_mes)

	if len(aux[aux['Variacao']<0].Variacao) > 0:
		sns.barplot(x=aux[aux['Variacao']<0].index , y='Variacao',data=aux[aux['Variacao']<0], order=order ,color='#D6675A', ax=ax_mes)

	canvas.draw()

	root.config(cursor='')
		

# Insert Enter Signal Button
def insert_enter_signal(e):
	txt = ' '+combobox_enter_signal.get()
	for p in entry_enter_signal_parameters:
		if p.get():
			txt += '('+p.get()+')'
	text_enter_setup.insert(END, txt.replace(')(',',')+' ')

# Insert Enter Conditional Button
def insert_enter_conditional(e):
	text_enter_setup.insert(END, ' '+combobox_enter_conditional.get().replace('(E)','').replace('(OU)','')+' ')

# Clear Enter Setup
def clear_enter_setup(e):
	text_enter_setup.delete('1.0', END)


# Insert quit Signal Button
def insert_quit_signal(e):
	txt = ' '+combobox_quit_signal.get()
	for p in entry_quit_signal_parameters:
		if p.get():
			txt += '('+p.get()+')'

	text_quit_setup.insert(END, txt.replace(')(',',')+' ')

# Insert quit Conditional Button
def insert_quit_conditional(e):
	text_quit_setup.insert(END, ' '+combobox_quit_conditional.get().replace('(E)','').replace('(OU)','')+' ')

# Clear quit Setup
def clear_quit_setup(e):
	text_quit_setup.delete('1.0', END)	

# Define parameters for different entry signal
def define_enter_signal_parameters(e):
	# Deixa todos os parametros inativos e com nomes p_..
	i = 1 
	for l,e in zip(label_enter_signal_labels,entry_enter_signal_parameters):
		l['text'] = 'p_'+str(i)
		e.delete(0, END)
		e['state'] = 'disabled'
		i+=1

	if combobox_enter_signal.get() in my_vars.candles_list:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

	elif combobox_enter_signal.get() in my_vars.gap_list:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

	elif combobox_enter_signal.get() in my_vars.one_moving_average_list[:2]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '25')
		label_enter_signal_labels[1]['text'] = 'Valor da Média:'

	elif combobox_enter_signal.get() in my_vars.one_moving_average_list[2:]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '25')
		label_enter_signal_labels[1]['text'] = 'Valor da Média:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '5')
		label_enter_signal_labels[2]['text'] = 'Valor de X:'

	elif combobox_enter_signal.get() in my_vars.two_moving_average_list[:2]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '25')
		label_enter_signal_labels[1]['text'] = 'Valor da Média 1:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '50')
		label_enter_signal_labels[2]['text'] = 'Valor da Média 2:'

	elif combobox_enter_signal.get() in my_vars.two_moving_average_list[2:]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '25')
		label_enter_signal_labels[1]['text'] = 'Valor da Média 1:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '50')
		label_enter_signal_labels[2]['text'] = 'Valor da Média 2:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '5')
		label_enter_signal_labels[3]['text'] = 'Valor de X:'

	elif combobox_enter_signal.get() in my_vars.didi_list:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '3')
		label_enter_signal_labels[1]['text'] = 'Valor da Média 1:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '8')
		label_enter_signal_labels[2]['text'] = 'Valor da Média 2:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '20')
		label_enter_signal_labels[3]['text'] = 'Valor da Média 3:'


	elif combobox_enter_signal.get() in my_vars.bollinger_list:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '20')
		label_enter_signal_labels[1]['text'] = 'Valor da Média:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '2')
		label_enter_signal_labels[2]['text'] = 'Valor de Std:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '5')
		label_enter_signal_labels[3]['text'] = 'Valor de X:'

	elif (combobox_enter_signal.get() in my_vars.MACD_list[:2]) or (combobox_enter_signal.get() in my_vars.HistMACD_list[:2]):
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '12')
		label_enter_signal_labels[1]['text'] = 'Valor da Média Curta:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '26')
		label_enter_signal_labels[2]['text'] = 'Valor da Média Longa:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '9')
		label_enter_signal_labels[3]['text'] = 'Valor de Sinal:'

	elif (combobox_enter_signal.get() in my_vars.MACD_list[2:]) or (combobox_enter_signal.get() in my_vars.HistMACD_list[2:]):
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '12')
		label_enter_signal_labels[1]['text'] = 'Valor da Média Curta:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '26')
		label_enter_signal_labels[2]['text'] = 'Valor da Média Longa:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '9')
		label_enter_signal_labels[3]['text'] = 'Valor de Sinal:'

		entry_enter_signal_parameters[4]['state'] = 'normal'
		entry_enter_signal_parameters[4].insert(0, '5')
		label_enter_signal_labels[4]['text'] = 'Valor de X:'

	elif combobox_enter_signal.get() in my_vars.ADX_list[:2]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '25')
		label_enter_signal_labels[1]['text'] = 'Valor de ADX:'

	elif combobox_enter_signal.get() in my_vars.ADX_list[2:]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '25')
		label_enter_signal_labels[1]['text'] = 'Valor de ADX:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '40')
		label_enter_signal_labels[2]['text'] = 'Valor de X:'

	elif combobox_enter_signal.get() in my_vars.stocastic_list[:2]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '20')
		label_enter_signal_labels[1]['text'] = 'Valor de Dias (N):'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '2')
		label_enter_signal_labels[2]['text'] = 'Valor de %K:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '5')
		label_enter_signal_labels[3]['text'] = 'Valor de %D:'

	elif combobox_enter_signal.get() in my_vars.stocastic_list[2:]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '14')
		label_enter_signal_labels[1]['text'] = 'Valor de Dias (N):'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '3')
		label_enter_signal_labels[2]['text'] = 'Valor de %K:'

		entry_enter_signal_parameters[3]['state'] = 'normal'
		entry_enter_signal_parameters[3].insert(0, '3')
		label_enter_signal_labels[3]['text'] = 'Valor de %D:'

		entry_enter_signal_parameters[4]['state'] = 'normal'
		entry_enter_signal_parameters[4].insert(0, '80')
		label_enter_signal_labels[4]['text'] = 'Valor de X:'

	elif combobox_enter_signal.get() in my_vars.volume_list[:2]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '14')
		label_enter_signal_labels[1]['text'] = 'Valor da Média:'

	elif combobox_enter_signal.get() in my_vars.volume_list[2:]:
		entry_enter_signal_parameters[0]['state'] = 'normal'
		entry_enter_signal_parameters[0].insert(0, '0')
		label_enter_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_enter_signal_parameters[1]['state'] = 'normal'
		entry_enter_signal_parameters[1].insert(0, '50')
		label_enter_signal_labels[1]['text'] = 'Valor da Média:'

		entry_enter_signal_parameters[2]['state'] = 'normal'
		entry_enter_signal_parameters[2].insert(0, '5')
		label_enter_signal_labels[2]['text'] = 'Valor de X:'

	else:
		for p in entry_enter_signal_parameters:
			p['state'] = 'disabled'

		i = 1 
		for l in label_enter_signal_labels:
			l['text'] = 'p_'+str(i)
			i+=1

# Define parameters for different quit signal
def define_quit_signal_parameters(e):
	# Deixa todos os parametros inativos e com nomes p_..
	i = 1 
	for l,e in zip(label_quit_signal_labels,entry_quit_signal_parameters):
		l['text'] = 'p_'+str(i)
		e.delete(0, END)
		e['state'] = 'disabled'
		i+=1

	if combobox_quit_signal.get() in my_vars.candles_list:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

	elif combobox_quit_signal.get() in my_vars.gap_list:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

	elif combobox_quit_signal.get() in my_vars.one_moving_average_list[:2]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '25')
		label_quit_signal_labels[1]['text'] = 'Valor da Média:'

	elif combobox_quit_signal.get() in my_vars.one_moving_average_list[2:]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '25')
		label_quit_signal_labels[1]['text'] = 'Valor da Média:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '5')
		label_quit_signal_labels[2]['text'] = 'Valor de X:'

	elif combobox_quit_signal.get() in my_vars.two_moving_average_list[:2]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '25')
		label_quit_signal_labels[1]['text'] = 'Valor da Média 1:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '50')
		label_quit_signal_labels[2]['text'] = 'Valor da Média 2:'

	elif combobox_quit_signal.get() in my_vars.two_moving_average_list[2:]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '25')
		label_quit_signal_labels[1]['text'] = 'Valor da Média 1:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '50')
		label_quit_signal_labels[2]['text'] = 'Valor da Média 2:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '5')
		label_quit_signal_labels[3]['text'] = 'Valor de X:'

	elif combobox_quit_signal.get() in my_vars.didi_list:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '3')
		label_quit_signal_labels[1]['text'] = 'Valor da Média 1:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '8')
		label_quit_signal_labels[2]['text'] = 'Valor da Média 2:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '20')
		label_quit_signal_labels[3]['text'] = 'Valor da Média 3:'


	elif combobox_quit_signal.get() in my_vars.bollinger_list:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '20')
		label_quit_signal_labels[1]['text'] = 'Valor da Média:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '2')
		label_quit_signal_labels[2]['text'] = 'Valor de Std:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '5')
		label_quit_signal_labels[3]['text'] = 'Valor de X:'

	elif (combobox_quit_signal.get() in my_vars.MACD_list[:2]) or (combobox_quit_signal.get() in my_vars.HistMACD_list[:2]):
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '12')
		label_quit_signal_labels[1]['text'] = 'Valor da Média Curta:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '26')
		label_quit_signal_labels[2]['text'] = 'Valor da Média Longa:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '9')
		label_quit_signal_labels[3]['text'] = 'Valor de Sinal:'

	elif (combobox_quit_signal.get() in my_vars.MACD_list[2:]) or (combobox_quit_signal.get() in my_vars.HistMACD_list[2:]):
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '12')
		label_quit_signal_labels[1]['text'] = 'Valor da Média Curta:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '26')
		label_quit_signal_labels[2]['text'] = 'Valor da Média Longa:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '9')
		label_quit_signal_labels[3]['text'] = 'Valor de Sinal:'

		entry_quit_signal_parameters[4]['state'] = 'normal'
		entry_quit_signal_parameters[4].insert(0, '5')
		label_quit_signal_labels[4]['text'] = 'Valor de X:'

	elif combobox_quit_signal.get() in my_vars.ADX_list[:2]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '25')
		label_quit_signal_labels[1]['text'] = 'Valor de ADX:'

	elif combobox_quit_signal.get() in my_vars.ADX_list[2:]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '25')
		label_quit_signal_labels[1]['text'] = 'Valor de ADX:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '40')
		label_quit_signal_labels[2]['text'] = 'Valor de X:'

	elif combobox_quit_signal.get() in my_vars.stocastic_list[:2]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '20')
		label_quit_signal_labels[1]['text'] = 'Valor de Dias (N):'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '2')
		label_quit_signal_labels[2]['text'] = 'Valor de %K:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '5')
		label_quit_signal_labels[3]['text'] = 'Valor de %D:'

	elif combobox_quit_signal.get() in my_vars.stocastic_list[2:]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '14')
		label_quit_signal_labels[1]['text'] = 'Valor de Dias (N):'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '3')
		label_quit_signal_labels[2]['text'] = 'Valor de %K:'

		entry_quit_signal_parameters[3]['state'] = 'normal'
		entry_quit_signal_parameters[3].insert(0, '3')
		label_quit_signal_labels[3]['text'] = 'Valor de %D:'

		entry_quit_signal_parameters[4]['state'] = 'normal'
		entry_quit_signal_parameters[4].insert(0, '80')
		label_quit_signal_labels[4]['text'] = 'Valor de X:'

	elif combobox_quit_signal.get() in my_vars.volume_list[:2]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '14')
		label_quit_signal_labels[1]['text'] = 'Valor da Média:'

	elif combobox_quit_signal.get() in my_vars.volume_list[2:]:
		entry_quit_signal_parameters[0]['state'] = 'normal'
		entry_quit_signal_parameters[0].insert(0, '0')
		label_quit_signal_labels[0]['text'] = 'Dia de ocorrência:'

		entry_quit_signal_parameters[1]['state'] = 'normal'
		entry_quit_signal_parameters[1].insert(0, '50')
		label_quit_signal_labels[1]['text'] = 'Valor da Média:'

		entry_quit_signal_parameters[2]['state'] = 'normal'
		entry_quit_signal_parameters[2].insert(0, '5')
		label_quit_signal_labels[2]['text'] = 'Valor de X:'

	else:
		for p in entry_quit_signal_parameters:
			p['state'] = 'disabled'

		i = 1 
		for l in label_quit_signal_labels:
			l['text'] = 'p_'+str(i)
			i+=1	
	

button_presentation = ttk.Button(root,
	style='info.TButton', text='Pressione este botão azul e AJUDE esta inciativa comprando o livro PYTHON E ANÁLISE TÉCNICA PARA A BOLSA DE VALORES\nou através do site: https://www.sclab.com.br/sclab-finc/TutorialPythonBook/')
button_presentation.pack(fill=X, expand=0, pady=0, padx=0, side=TOP)
button_presentation.bind('<Button-1>', open_book_site)

# Create Notebook to insert TABS
my_notebook = ttk.Notebook(root)#, width=500, height=500)
my_notebook.pack(fill=BOTH, expand=1, pady=0, side=BOTTOM)

# Create Frames for notebook
cotation_tab = ttk.Frame(my_notebook)#, width=500, height=500)
result_tab = ttk.Frame(my_notebook)#, width=500, height=500)
about_tab = ttk.Frame(my_notebook)#, width=500, height=500)


#### COTATION BAR #####
# Create Canvas for ScrollBar
cotation_canvas = Canvas(cotation_tab)
cotation_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add Scrollbal to the Canvas
cotation_scrollbar = ttk.Scrollbar(cotation_tab, orient=VERTICAL, command=cotation_canvas.yview)
cotation_scrollbar.pack(side=RIGHT, fill=Y)

# Configure Canvas
cotation_canvas.configure(yscrollcommand=cotation_scrollbar.set)
cotation_canvas.bind('<Configure>', FrameWidth)

# Create another frame inside the canvas
# All object must be insert here
cotation_frame = Frame(cotation_canvas)
# cotation_frame.pack(fill=BOTH, expand=1)

# add that new frame to a window
cf = cotation_canvas.create_window((0,0), window=cotation_frame, anchor='nw')#, width=600)


## PRICES
# Import prices Frame
labelframe = ttk.LabelFrame(cotation_frame, text="Cotações:")
labelframe.pack(fill=BOTH, expand=1)

# Select prices source combobox
combobox_select_source = ttk.Combobox(labelframe, state='readonly', textvariable=StringVar(), values=['Cotação Yahoo-finance','Minhas próprias cotações'])
combobox_select_source.grid(row=0, column=0, pady=pady, padx=padx, sticky='nsew')
combobox_select_source.current(1)

combobox_select_source.bind('<<ComboboxSelected>>', change_source_prices)

##############################
# IMPORT YAHOO FINANCE TICKERS
##############################

# Instructions Label 
label_instructions = ttk.Label(labelframe, text='A disposição das colunas de dados deve ser: Data | Abertura | Máxima | Fechamento | Volume\nO separador decimal deve ser o ponto "."')
# label_instructions = ttk.Label(labelframe, text='As cotações possuem os mesmos símbolos do site Yahoo Finance. Após escolher o ativo, deve-se definir o período e o intervalo.\nÉ importante lembrar que os valores tipo "NAN" são deletados, nenhum outro tratamento é feito sobre os dados do Yahoo Finance.')
label_instructions.grid(row=2, column=0, columnspan=3, pady=pady, padx=padx,sticky='nsew')

# Yahoo-Finance Parameters Paper
combobox_select_paper = ttk.Combobox(labelframe, textvariable=StringVar(), values=my_vars.symbols)
# combobox_select_paper.grid(row=3, column=0, pady=pady, padx=padx, sticky='nsew')
combobox_select_paper.set('Escolha o ativo')

# Yahoo-Finance Parameters Period
combobox_select_period = ttk.Combobox(labelframe, textvariable=StringVar(), values=my_vars.period)
# combobox_select_period.grid(row=3, column=1, pady=pady, padx=padx, sticky='nsew')
combobox_select_period.set('Escolha o período do histórico')
combobox_select_period.bind('<<ComboboxSelected>>', change_timeframe)

# Yahoo-Finance Parameters Timeframe
combobox_select_timeframe = ttk.Combobox(labelframe, textvariable=StringVar(), values=my_vars.timeframe)
# combobox_select_timeframe.grid(row=3, column=2, pady=pady, padx=padx, sticky='nsew')
combobox_select_timeframe.set('Escolha o timeframe')



# Grid.columnconfigure(labelframe, 0, weight=1)
# Grid.columnconfigure(labelframe, 1, weight=1)
# Grid.columnconfigure(labelframe, 2, weight=1)


# label_instructions['text'] = 'A disposição das colunas de dados deve ser: Data | Abertura | Máxima | Mínima | Fechamento | Volume\nO separador decimal deve ser o ponto "."'
# Must be showed
# checkbutton_intraday.grid(row=1, column=0, pady=pady, padx=padx,sticky='nsew')
# button_openFile.grid(row=3, column=0, pady=pady, padx=padx,sticky='nsew')
# entry_filePath.grid(row=3, column=1, columnspan=2, pady=pady, padx=padx, sticky='nsew')
# combobox_codec.grid(row=4, column=0, pady=pady, padx=padx,sticky='nsew')
# combobox_delimiter.grid(row=4, column=1, pady=pady, padx=padx, sticky='nsew')
# combobox_date_fmt.grid(row=4, column=2, pady=pady, padx=padx, sticky='nsew')


# #######################
# IMPORT OWN FILES
# #####################
# Intraday CheckButton
# checkbutton_intraday = ttk.Checkbutton(labelframe, text='Intraday')
# checkbutton_intraday.bind('<<Checkbutton>>', )

# # Instructions Label 
# label_instructions = ttk.Label(labelframe, text='A disposição das colunas de dados deve ser: Data | Abertura | Máxima | Fechamento | Volume\nO separador decimal deve ser o ponto "."')
# label_instructions.grid(row=1, column=0, columnspan=3, pady=pady, padx=padx,sticky='nsew')

# Import File Button
button_openFile = ttk.Button(labelframe, text='Abrir arquivo de cotações', command=open_file)
button_openFile.grid(row=3, column=0, pady=pady, padx=padx,sticky='nsew')

# # File Path Text
entry_filePath = Entry(labelframe, state='readonly')
entry_filePath.grid(row=3, column=1, columnspan=2, pady=pady, padx=padx, sticky='nsew')

# # Codec Combobox
combobox_codec = ttk.Combobox(labelframe, state='readonly', textvariable=StringVar(), values=my_vars.codec)
combobox_codec.grid(row=4, column=0, pady=pady, padx=padx,sticky='nsew')
# combobox_codec.delete(0)
combobox_codec.set('Codecs')

# # Delimiter Combobox
combobox_delimiter = ttk.Combobox(labelframe, state='readonly', textvariable=StringVar(), values=my_vars.delimiter)
combobox_delimiter.grid(row=4, column=1, pady=pady, padx=padx, sticky='nsew')
combobox_delimiter.set('Delimitador')

# # Date Combobox
combobox_date_fmt = ttk.Combobox(labelframe, state='readonly', textvariable=StringVar(), values=['Dia Mês Ano', 'Ano Mês Dia'])
combobox_date_fmt.grid(row=4, column=2, pady=pady, padx=padx, sticky='nsew')
combobox_date_fmt.set('Formato da Data')


# # Config our cols and rows for buttons
Grid.rowconfigure(labelframe, 0, weight=1)
Grid.rowconfigure(labelframe, 1, weight=1)
Grid.rowconfigure(labelframe, 2, weight=1)
Grid.rowconfigure(labelframe, 3, weight=1)

Grid.columnconfigure(labelframe, 0, weight=1)
Grid.columnconfigure(labelframe, 1, weight=3)
Grid.columnconfigure(labelframe, 2, weight=1)

# ###########################################


## OPERATIONS DATA
# operations Data Frame
labelframe_op = ttk.LabelFrame(cotation_frame, text="Dados da Operação:")
labelframe_op.pack(fill=BOTH, expand=1, pady=15)

# Date Combobox
combobox_op_type = ttk.Combobox(labelframe_op, state='readonly', textvariable=StringVar(), values=['Comprado e vendido', 'Comprado', 'Vendido'])
combobox_op_type.grid(row=0, column=0, pady=pady, padx=padx, sticky='nsew')
combobox_op_type.current(0)

# Validade Combobox
combobox_op_validate = ttk.Combobox(labelframe_op, state='readonly', textvariable=StringVar(), values=['Normal', 'DayTrade'])
combobox_op_validate.grid(row=0, column=1, pady=pady, padx=padx, sticky='nsew')
combobox_op_validate.current(0)

# Enter Price
combobox_op_enterprice = ttk.Combobox(labelframe_op, state='readonly', textvariable=StringVar(), values=my_vars.enter_prices)
combobox_op_enterprice.grid(row=0, column=2, pady=pady, padx=padx, sticky='nsew')
combobox_op_enterprice.current(0)

# Enter Day
spinbox_op_enterday = ttk.Spinbox(labelframe_op, state='readonly', from_=0, to=100, textvariable=StringVar(value=1), wrap=True)
spinbox_op_enterday.grid(row=0, column=3, pady=pady, padx=padx, sticky='nsew')
spinbox_op_enterday.set(1)

# Quit Price
combobox_op_quitprice = ttk.Combobox(labelframe_op, state='readonly', textvariable=StringVar(), values=my_vars.quit_prices)
combobox_op_quitprice.grid(row=1, column=2, pady=pady, padx=padx, sticky='nsew')
combobox_op_quitprice.current(1)

# Quit Day
spinbox_op_quitday = ttk.Spinbox(labelframe_op, state='readonly', from_=0, to=100, textvariable=StringVar(value=1), wrap=True)
spinbox_op_quitday.grid(row=1, column=3, pady=pady, padx=padx, sticky='nsew')
spinbox_op_quitday.set(0)

# Contract size Label
label_contract_size = ttk.Label(labelframe_op, text='Quantidade de ativos:')
label_contract_size.grid(row=1, column=0, pady=pady, padx=padx,sticky='nsew')

# Contract size spinbox
spinbox_contract_size = ttk.Spinbox(labelframe_op, state='readonly', from_=1, to=1000000, textvariable=StringVar(value=1), wrap=False)
spinbox_contract_size.grid(row=1, column=1, pady=pady, padx=padx, sticky='nsew')
spinbox_contract_size.set(1)

# Contract fee Label
label_contract_fee = ttk.Label(labelframe_op, text='Custo/Operação:')
label_contract_fee.grid(row=2, column=0, pady=pady, padx=padx,sticky='nsew')

# Contract fee spinbox
spinbox_contract_fee = ttk.Spinbox(labelframe_op, state='normal', from_=0, to=1000000, textvariable=StringVar(value=0.25), wrap=False)
spinbox_contract_fee.grid(row=2, column=1, pady=pady, padx=padx, sticky='nsew')
spinbox_contract_fee.set(0)

Grid.columnconfigure(labelframe_op, 0, weight=2)
Grid.columnconfigure(labelframe_op, 1, weight=2)
Grid.columnconfigure(labelframe_op, 2, weight=4)
Grid.columnconfigure(labelframe_op, 3, weight=1)



## SETUP ENTER
# Enter setup Frame
labelframe_enter_setup = ttk.LabelFrame(cotation_frame, text="Setup de entrada:")
labelframe_enter_setup.pack(fill=BOTH, expand=1, pady=15)#, padx=(0,10), side=LEFT)

# Enter Signal Label
label_choose_enter_signal = ttk.Label(labelframe_enter_setup, text='Escolha o sinal e os parâmetros:')
label_choose_enter_signal.grid(row=0, column=0, columnspan=5, pady=pady, padx=padx, sticky='nsew')

# Enter Signal Combobox
combobox_enter_signal = ttk.Combobox(labelframe_enter_setup, state='readonly', textvariable=StringVar(), values=my_vars.all_signals)
combobox_enter_signal.grid(row=1, column=1, columnspan=5, pady=pady, padx=padx, sticky='nsew')
combobox_enter_signal.set('')
combobox_enter_signal.bind('<<ComboboxSelected>>', define_enter_signal_parameters)

# Enter Signal entry
label_enter_signal_labels = []
entry_enter_signal_parameters = []
for eesp in range(1,6):
	label_enter_signal_labels.append(ttk.Label(labelframe_enter_setup, text='p_'+str(eesp)+':',) )
	entry_enter_signal_parameters.append(ttk.Entry(labelframe_enter_setup, state='disabled'))
	if eesp==1:
		label_enter_signal_labels[-1].grid(row=2, column=eesp, pady=(pady, 0), padx=(padx,1), sticky='nsew')
		entry_enter_signal_parameters[-1].grid(row=3, column=eesp, pady=pady, padx=(padx,1), sticky='nsew')
	elif eesp==5:
		label_enter_signal_labels[-1].grid(row=2, column=eesp, pady=(pady,0), padx=(1,padx), sticky='nsew')
		entry_enter_signal_parameters[-1].grid(row=3, column=eesp, pady=pady, padx=(1,padx), sticky='nsew')
	else:
		label_enter_signal_labels[-1].grid(row=2, column=eesp, pady=(pady,0), padx=1, sticky='nsew')
		entry_enter_signal_parameters[-1].grid(row=3, column=eesp, pady=pady, padx=1, sticky='nsew')

# Insert Signal Button
button_insert_enter_signal = ttk.Button(labelframe_enter_setup, text='Inserir Sinal')
button_insert_enter_signal.grid(row=1,rowspan=3, column=6, pady=pady, padx=padx, sticky='nsew')
button_insert_enter_signal.bind('<Button-1>', insert_enter_signal)



# Enter Conditional Label
label_choose_enter_conditional = ttk.Label(labelframe_enter_setup, text='Escolha a condicional:')
label_choose_enter_conditional.grid(row=4, column=0, columnspan=3, pady=pady, padx=padx, sticky='nsew')

# Enter Conditional Combobox
combobox_enter_conditional = ttk.Combobox(labelframe_enter_setup, state='readonly', textvariable=StringVar(), values=['&(E)', '|(OU)'])
combobox_enter_conditional.grid(row=4, column=3, columnspan=3, pady=pady, padx=(1, padx), sticky='nsew')
combobox_enter_conditional.current(0)

# Insert Conditional Button
button_insert_enter_conditional = ttk.Button(labelframe_enter_setup, text='Inserir Condicional')
button_insert_enter_conditional.grid(row=4, column=6, pady=pady, padx=padx, sticky='nsew')
button_insert_enter_conditional.bind('<Button-1>', insert_enter_conditional)


# Text Enter Setup
label_enter_setup = ttk.Label(labelframe_enter_setup, text='Setup de entrada (abertura de posição):')
label_enter_setup.grid(row=5, column=0, columnspan=6, pady=(pady+15,pady), padx=padx, sticky='nsew')

button_clear_enter_setup = ttk.Button(labelframe_enter_setup, text='Limpar Setup', style='danger.TButton')
button_clear_enter_setup.grid(row=5, column=6, pady=(pady+15,pady), padx=padx, sticky='nsew')
button_clear_enter_setup.bind('<Button-1>', clear_enter_setup)

text_enter_setup = Text(labelframe_enter_setup, height=10)
text_enter_setup.grid(row=6, column=0, columnspan=7, pady=pady, padx=padx, sticky='nsew')


Grid.columnconfigure(labelframe_enter_setup, 0, weight=1)
Grid.columnconfigure(labelframe_enter_setup, 1, weight=4)
Grid.columnconfigure(labelframe_enter_setup, 2, weight=4)
Grid.columnconfigure(labelframe_enter_setup, 3, weight=4)
Grid.columnconfigure(labelframe_enter_setup, 4, weight=4)
Grid.columnconfigure(labelframe_enter_setup, 5, weight=4)
Grid.columnconfigure(labelframe_enter_setup, 6, weight=4)




## SETUP QUIT
# Quit setup Frame
labelframe_quit_setup = ttk.LabelFrame(cotation_frame, text="Setup de saída:")
labelframe_quit_setup.pack(fill=BOTH, expand=1, pady=15)#, padx=(0,10), side=LEFT)

# Quit Signal Label
label_choose_quit_signal = ttk.Label(labelframe_quit_setup, text='Escolha o sinal e os parâmetros:')
label_choose_quit_signal.grid(row=0, column=0, columnspan=5, pady=pady, padx=padx, sticky='nsew')

# Quit Signal Combobox
combobox_quit_signal = ttk.Combobox(labelframe_quit_setup, state='readonly', textvariable=StringVar(), values=my_vars.all_signals)
combobox_quit_signal.grid(row=1, column=1, columnspan=5, pady=pady, padx=padx, sticky='nsew')
combobox_quit_signal.set('')
combobox_quit_signal.bind('<<ComboboxSelected>>', define_quit_signal_parameters)

# Quit Signal entry
label_quit_signal_labels = []
entry_quit_signal_parameters = []
for eesp in range(1,6):
	label_quit_signal_labels.append(ttk.Label(labelframe_quit_setup, text='p_'+str(eesp)+':',) )
	entry_quit_signal_parameters.append(ttk.Entry(labelframe_quit_setup, state='normal'))
	if eesp==1:
		label_quit_signal_labels[-1].grid(row=2, column=eesp, pady=(pady, 0), padx=(padx,1), sticky='nsew')
		entry_quit_signal_parameters[-1].grid(row=3, column=eesp, pady=pady, padx=(padx,1), sticky='nsew')
	elif eesp==5:
		label_quit_signal_labels[-1].grid(row=2, column=eesp, pady=(pady,0), padx=(1,padx), sticky='nsew')
		entry_quit_signal_parameters[-1].grid(row=3, column=eesp, pady=pady, padx=(1,padx), sticky='nsew')
	else:
		label_quit_signal_labels[-1].grid(row=2, column=eesp, pady=(pady,0), padx=1, sticky='nsew')
		entry_quit_signal_parameters[-1].grid(row=3, column=eesp, pady=pady, padx=1, sticky='nsew')

# Insert Signal Button
button_insert_quit_signal = ttk.Button(labelframe_quit_setup, text='Inserir Sinal')
button_insert_quit_signal.grid(row=1,rowspan=3, column=6, pady=pady, padx=padx, sticky='nsew')
button_insert_quit_signal.bind('<Button-1>', insert_quit_signal)


# Enter Conditional Label
label_choose_quit_conditional = ttk.Label(labelframe_quit_setup, text='Escolha a condicional:')
label_choose_quit_conditional.grid(row=4, column=0, columnspan=3, pady=pady, padx=padx, sticky='nsew')

# Enter Conditional Combobox
combobox_quit_conditional = ttk.Combobox(labelframe_quit_setup, state='readonly', textvariable=StringVar(), values=['&(E)', '|(OU)'])
combobox_quit_conditional.grid(row=4, column=3, columnspan=3, pady=pady, padx=(1, padx), sticky='nsew')
combobox_quit_conditional.current(0)

# Insert Conditional Button
button_insert_quit_conditional = ttk.Button(labelframe_quit_setup, text='Inserir Condicional')
button_insert_quit_conditional.grid(row=4, column=6, pady=pady, padx=padx, sticky='nsew')
button_insert_quit_conditional.bind('<Button-1>', insert_quit_conditional)

# Text Enter Setup
label_quit_setup = ttk.Label(labelframe_quit_setup, text='Setup de entrada (abertura de posição):')
label_quit_setup.grid(row=5, column=0, columnspan=6, pady=(pady+15,pady), padx=padx, sticky='nsew')

button_clear_quit_setup = ttk.Button(labelframe_quit_setup, text='Limpar Setup', style='danger.TButton')
button_clear_quit_setup.grid(row=5, column=6, pady=(pady+15,pady), padx=padx, sticky='nsew')
button_clear_quit_setup.bind('<Button-1>', clear_quit_setup)

text_quit_setup = Text(labelframe_quit_setup, height=10)
text_quit_setup.grid(row=6, column=0, columnspan=7, pady=pady, padx=padx, sticky='nsew')


Grid.columnconfigure(labelframe_quit_setup, 0, weight=1)
Grid.columnconfigure(labelframe_quit_setup, 1, weight=4)
Grid.columnconfigure(labelframe_quit_setup, 2, weight=4)
Grid.columnconfigure(labelframe_quit_setup, 3, weight=4)
Grid.columnconfigure(labelframe_quit_setup, 4, weight=4)
Grid.columnconfigure(labelframe_quit_setup, 5, weight=4)
Grid.columnconfigure(labelframe_quit_setup, 6, weight=4)


button_generate_report = ttk.Button(cotation_frame, text='Calcular e Gerar Dados Estatísticos de Backtest', style='primary.TButton')
button_generate_report.pack(fill=BOTH, expand=1, pady=15)
button_generate_report.bind('<Button-1>', gera_calcula_backtest)

label_COPYRIGTH = ttk.Label(cotation_frame, text='')
label_COPYRIGTH.pack(fill=BOTH, expand=1, pady=15)




#####################


## WARNING
warning = """\nATENÇÃO:\n\nEste relatório não é (e não deve ser considerado) um indicativo de compra ou venda de ativos na bolsa de valores, e também não objetiva gerenciar carteria de ativos, uma vez que não seleciona ativos e não envia ordens. Aqui foram avaliados dados históricos para se chegar ao resultado de backtesting, ou seja, nosso algorítmo avalia a performance de sua estratégia apenas com dados do passado (portanto, desatualizados) o que não garante, de maneira alguma, o comportamento futuro do ativo em questão. Caso esteja procurando um relatório que indique e aconselhe uma tomada de decisão, abertura ou fechamento de operação, procure um profissional de investimento especializado e regulamentado pela CVM e APIMEC com certificação CNPI. """
text_warning = ttk.Label(result_tab, text=warning, wraplength=965, style='danger.TLabel')#, height=7, )
# text_warning.insert('end',warning)
text_warning.pack(fill=X, expand=0, pady=(0,15)) #fill=X, expand=0, pady=0, padx=0, side=TOP


buttons_frame = ttk.Frame(result_tab)
buttons_frame.pack(fill=X, expand=0)

# Save report
button_save_basic_report = ttk.Button(buttons_frame, text='Salvar relatório básico', command=save_basic_report_file)
button_save_basic_report.grid(row=0, column=0, pady=pady, padx=padx,sticky='nsew')

# Save history
button_save_backtesting = ttk.Button(buttons_frame, text='Salvar backtesting', command=save_backtesting_file)
button_save_backtesting.grid(row=0, column=1, pady=pady, padx=padx,sticky='nsew')

# Save history
button_save_history = ttk.Button(buttons_frame, text='Salvar cotações e indicadores', command=save_cotation_file)
button_save_history.grid(row=0, column=2, pady=pady, padx=padx,sticky='nsew')


#### RESULT BAR #####
# Create Canvas for ScrollBar
result_canvas = Canvas(result_tab)
result_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add Scrollbal to the Canvas
result_scrollbar = ttk.Scrollbar(result_tab, orient=VERTICAL, command=result_canvas.yview)
result_scrollbar.pack(side=RIGHT, fill=Y)

# Configure Canvas
result_canvas.configure(yscrollcommand=result_scrollbar.set)
# cotation_canvas.bind('<Configure>', lambda e: cotation_canvas.configure(scrollregion=cotation_canvas.bbox('all')))
result_canvas.bind('<Configure>', FrameWidth)


# Create another frame inside the canvas
# All object must be insert here
result_frame = Frame(result_canvas)
# cotation_frame.pack(fill=BOTH, expand=1)

# add that new frame to a window
rf = result_canvas.create_window((0,0), window=result_frame, anchor='nw')#, width=600)


## BASIC REPORT
# Text report
textreportframe = ttk.LabelFrame(result_frame, text="Relatório Básico:")
textreportframe.pack(fill=BOTH, expand=1, pady=15)

# Report Label 
label_report = ttk.Label(textreportframe, text='Nada foi calculado ainda!!! \t\n\n\n')
label_report.grid(row=0, column=0, columnspan=3, pady=pady, padx=padx, sticky='nsew')

img_notstonks = ImageTk.PhotoImage(Image.open('img/notstonks.png').resize((290, 217)) )
img_stonks = ImageTk.PhotoImage(Image.open('img/stonks.png').resize((290, 217)) )
panel = Label(textreportframe, image = img_stonks)
panel.grid(row=0,column=4, pady=pady, padx=padx, sticky='nsew')#, expand = "yes")


# PLOTS REPORT
# plots report
plotreportframe = ttk.LabelFrame(result_frame, text="Relatórios Gráficos:")
plotreportframe.pack(fill=BOTH, expand=1)

# Report Label 
# label_plots = ttk.Label(plotreportframe, text='Total de operações: \t\n\n\n')
# label_plots.grid(row=0, column=0, columnspan=3, pady=pady, padx=padx, sticky='nsew')



# Plots
sns.set_style("whitegrid")
fig = plt.Figure(figsize=(10, 20), dpi=100, tight_layout=True)
t = np.arange(0, 3, .01)
ax_pizza = fig.add_subplot(5,2,1)
ax_barra = fig.add_subplot(5,2,2)
ax_histograma = fig.add_subplot(5,2,3)
ax_scatter = fig.add_subplot(5,2,4)
ax_linha = fig.add_subplot(5,2,(5,6))
ax_hora = fig.add_subplot(5,2,7)
ax_semana = fig.add_subplot(5,2,8)
ax_mes = fig.add_subplot(5,2,(9,10))

canvas = FigureCanvasTkAgg(fig, master=plotreportframe)  # A tk.DrawingArea.


canvas.draw()
# canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, plotreportframe)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)



## SOBRE
#### SOBRE BAR #####
# Create Canvas for ScrollBar
about_canvas = Canvas(about_tab)
about_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add Scrollbal to the Canvas
about_scrollbar = ttk.Scrollbar(about_tab, orient=VERTICAL, command=about_canvas.yview)
about_scrollbar.pack(side=RIGHT, fill=Y)

# Configure Canvas
about_canvas.configure(yscrollcommand=about_scrollbar.set)
# cotation_canvas.bind('<Configure>', lambda e: cotation_canvas.configure(scrollregion=cotation_canvas.bbox('all')))
about_canvas.bind('<Configure>', FrameWidth)


# Create another frame inside the canvas
# All object must be insert here
about_frame = Frame(about_canvas)
# cotation_frame.pack(fill=BOTH, expand=1)

# add that new frame to a window
af = about_canvas.create_window((0,0), window=about_frame, anchor='nw')

sobre = """
\u2022 COMO AJUDAR?

- Compre o livro de PYTHON E ANÁLISE TÉCNICA PARA A BOLSA DE VALORES (botão azul na região superior a tela)
- Corrija erros e bugs, insira novas funcinalidades ou melhore o código através do repositório https://github.com/guilhermetabordaribas/MoneyMapSCLAB
- Divulgue esta iniciativa

\u2022 ORIENTAÇÃO GERAL:\n
Este software, projetado em Python 3.8.10, foi elaborado para auxiliar nos estudos e pesquisas sobre a análise técnica na bolsa de valores. Seu propósito é integralmente educacional, para tanto, disponibilzamos gratuitamente em com seu código aberto para que o pesquisador/estudante tenha livre acesso ás informações contidas no programa.

Este programa ainda está em sua versão BETA de testes, contamos com sua colaboração para ajudar a corrigir possíveis erros e bugs. Caso encontre algum erro ou tenha alguma sugestão, por favor, informe através do repositório https://github.com/guilhermetabordaribas/MoneyMapSCLAB

\u2022 VERSÃO: SCLAB MoneyMap Backtesting - BETA 6.0

\u2022 PACOTES UTILIZADOS:

- scipy==1.7.1
- numpy==1.21.2
- pandas==1.3.2
- matplotlib==3.4.3
- seaborn==0.11.2	
- ttkbootstrap==0.5.1
- yfinance==0.1.63

\u2022 LICENÇA: LGPL v3

Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo sob os termos da GNU Lesser General Public License (LGPL) publicada pela Free Software Foundation (FSF), na versão 3 da licença.

Este programa é distribuído na esperança de que possa ser útil, mas SEM NENHUMA GARANTIA; sem garantia implícita de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a GNU LGPL (Lesser General Public License) para mais detalhes.
Veja a cópia dessa licença em sua língua original em: www.gnu.org/licenses/

\u2022 AVISO LEGAL IMPORTANTE:\n
Este programa utiliza o pacote yfinance, o qual utiliza API Yahoo!, Y!Finance, e Yahoo! finance registradas sob a marca Yahoo, Inc. 

A iniciativa Sclab não é afiliada, endosada ou verificada pela Yahoo, Inc. Este programa é uma ferramenta de código aberto que usa APIs disponíveis publicamente do Yahoo e se destina a fins edicacionais e de pesquisa.
Você deve consultar os termos de uso do Yahoo! para obter detalhes sobre seus direitos de uso dos dados reais baixados. Lembre-se-o Yahoo! API de finanças destina-se apenas ao uso pessoal.

Termos de uso do Yahoo!:

	- https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm
	- https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html
	- https://policies.yahoo.com/us/en/yahoo/terms/index.htm
"""
text_sobre = ttk.Label(about_frame, text=sobre, wraplength=1000)#, style='primary.TLabel')#, height=7, )
# text_warning.insert('end',warning)
text_sobre.pack(fill=X, expand=0, pady=(0,15)) #fill=X, expand=0, pady=0, padx=0, side=TOP

cotation_tab.pack(fill=BOTH, expand=1)
result_tab.pack(fill=BOTH, expand=1)
about_tab.pack(fill=BOTH, expand=1)

my_notebook.add(cotation_tab, text='Dados Gerais')
my_notebook.add(result_tab, text='Resultados')
my_notebook.add(about_tab, text='Sobre')

root.mainloop()



