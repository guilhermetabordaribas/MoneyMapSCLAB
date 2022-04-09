"""
Copyright (c) 2021 Guilherme Taborda Ribas All rights reserved.

Copyright (c) 2012-2013 Matplotlib Development Team; All Rights Reserved.

Copyright (c) 2017 NumPy developers.

Copyright (c) 2021, Israel Dryer. Revision b35a9984 .

Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
All rights reserved.

Copyright (c) 2001-2002 Enthought, Inc.  2003-2019, SciPy Developers.
All rights reserved.

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

import numpy as np
import pandas as pd

################
##CANDLESTICKS##
################
def doji(df, p):
	name = 'Doji('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = df['Close'].shift(abs(bar)) == df['Open'].shift(abs(bar))

def martelo_alta(df, p):
	name = 'Martelo_Alta('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Open'].shift(abs(bar))<df['Close'].shift(abs(bar))) & \
		(df['Close'].shift(abs(bar))==df['High'].shift(abs(bar))) & \
		((df['Close'].shift(abs(bar))-df['Open'].shift(abs(bar)))<=(df['Open'].shift(abs(bar))-df['Low'].shift(abs(bar)) )/2)

def martelo_baixa(df, p):
	name = 'Martelo_Baixa('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Open'].shift(abs(bar))>df['Close'].shift(abs(bar))) & \
		(df['Open'].shift(abs(bar))==df['High'].shift(abs(bar))) & \
		((df['Open'].shift(abs(bar))-df['Close'].shift(abs(bar)))<=(df['Close'].shift(abs(bar))-df['Low'].shift(abs(bar)))/2)

def martelo(df, p):
	name = 'Martelo('+p+')'

	bar = int(p.split(',')[0])

	# It'to avoid recalculation
	if 'Martelo_Alta('+p+')' not in df.columns:
		martelo_alta(df, p)
	if 'Martelo_Baixa('+p+')' not in df.columns:
		martelo_baixa(df, p)
	
	if name not in df.columns: 
		df[name] = df['Martelo_Alta('+p+')'] | df['Martelo_Baixa('+p+')']

def estrela_cadente_alta(df, p):
	name = 'Estrela_Cadente_Alta('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Open'].shift(abs(bar))<df['Close'].shift(abs(bar))) & \
		(df['Open'].shift(abs(bar))==df['High'].shift(abs(bar))) & \
		((df['Close'].shift(abs(bar))-df['Open'].shift(abs(bar)))<=(df['High'].shift(abs(bar))-df['Close'].shift(abs(bar)))/2)

def estrela_cadente_baixa(df, p):
	name = 'Estrela_Cadente_Baixa('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Open'].shift(abs(bar))>df['Close'].shift(abs(bar))) & \
		(df['Close'].shift(abs(bar))==df['High'].shift(abs(bar))) & \
		((df['Open'].shift(abs(bar))-df['Close'].shift(abs(bar)))<=(df['High'].shift(abs(bar))-df['Open'].shift(abs(bar)))/2)

def estrela_cadente(df, p):
	name = 'Estrela_Cadente('+p+')'

	bar = int(p.split(',')[0])

	if 'Estrela_Cadente_Alta('+p+')' not in df.columns:
		estrela_cadente_alta(df, p)
	if 'Estrela_Cadente_Baixa('+p+')' not in df.columns:
		estrela_cadente_baixa(df, p)
	
	if name not in df.columns: 
		df[name] = df['Estrela_Cadente_Baixa('+p+')'] | df['Estrela_Cadente_Alta('+p+')']

def engolfo_de_alta(df, p):
	name = 'Engolfo_de_Alta('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Open'].shift(abs(bar))<df['Close'].shift(abs(bar))) & \
		(df['Open'].shift(1+abs(bar))>=df['Close'].shift(1+abs(bar))) & \
		(df['Open'].shift(abs(bar))<df['Open'].shift(1+abs(bar))) & \
		(df['Open'].shift(1+abs(bar))<df['Close'].shift(abs(bar))) & \
		(df['Open'].shift(abs(bar))<df['Close'].shift(1+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))<df['Close'].shift(abs(bar)))

def engolfo_de_baixa(df, p):
	name = 'Engolfo_de_Baixa('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Open'].shift(abs(bar))>df['Close'].shift(abs(bar))) & \
		(df['Open'].shift(1+abs(bar))<=df['Close'].shift(1+abs(bar))) & \
		(df['Open'].shift(abs(bar))>df['Open'].shift(1+abs(bar))) & \
		(df['Open'].shift(1+abs(bar))>df['Close'].shift(abs(bar))) & \
		(df['Open'].shift(abs(bar))>df['Close'].shift(1+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))>df['Close'].shift(abs(bar)))
		
def engolfo(df, p):
	bar = int(p.split(',')[0])
	if 'Engolfo_de_Alta('+p+')' not in df.columns:
		engolfo_de_alta(df, p)
	if 'Engolfo_de_Baixa('+p+')' not in df.columns:
		engolfo_de_baixa(df, p)
	
	df['Engolfo('+p+')'] = df['Engolfo_de_Alta('+p+')'] | df['Engolfo_de_Baixa('+p+')']

def piercing_line(df, p):
	name = 'Piercing_Line('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))>df['Open'].shift(abs(bar))) & \
		(df['Open'].shift(abs(bar))<df['Close'].shift(1+abs(bar))) & \
		(df['Close'].shift(abs(bar))>=(df['Close'].shift(1+abs(bar))+ df['Open'].shift(1+abs(bar)))/2) & \
		(df['Close']<=df['Open'].shift(1+abs(bar)))

###A partir daqui, nenhuma def de candles foi testada, verificar isso tudo.
def dark_cloud_cover(df, p):
	name = 'Dark_Cloud_Cover('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))<df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(1+abs(bar))>df['Open'].shift(1+abs(bar))) & \
		(df['Open'].shift(abs(bar))>df['Close'].shift(1+abs(bar))) & \
		(df['Close'].shift(abs(bar))<=(df['Close'].shift(1+abs(bar))+ df['Open'].shift(1+abs(bar)))/2) & \
		(df['Close']>=df['Open'].shift(1+abs(bar)))

def harami_de_fundo(df, p):
	name = 'Harami_de_Fundo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))>df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(1+abs(bar))<df['Open'].shift(1+abs(bar))) & \
		(df['Open'].shift(abs(bar))>df['Close'].shift(1+abs(bar))) & \
		(df['Close'].shift(abs(bar))<df['Open'].shift(1+abs(bar))) & \
		((df['Close'].shift(abs(bar))-df['Open'].shift(abs(bar)))<=((df['Open'].shift(1+abs(bar))-df['Close'].shift(1+abs(bar)))/4))

def harami_de_topo(df, p):
	name = 'Harami_de_Topo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))<df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(1+abs(bar))>df['Open'].shift(1+abs(bar))) & \
		(df['Open'].shift(abs(bar))<df['Close'].shift(1+abs(bar))) & \
		(df['Close'].shift(abs(bar))>df['Open'].shift(1+abs(bar))) & \
		((df['Open'].shift(abs(bar))-df['Close'].shift(abs(bar)))<=((df['Close'].shift(1+abs(bar))-df['Open'].shift(1+abs(bar)))/4))

def ave_migratoria_de_fundo(df, p):
	name = 'Ave_Migratoria_de_Fundo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))<df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(1+abs(bar))<df['Open'].shift(1+abs(bar))) & \
		(df['Open'].shift(abs(bar))<df['Open'].shift(1+abs(bar))) & \
		(df['Close'].shift(abs(bar))>df['Close'].shift(1+abs(bar))) & \
		((df['Open'].shift(abs(bar))-df['Close'].shift(abs(bar)))<=((df['Open'].shift(1+abs(bar))-df['Close'].shift(1+abs(bar)))/4))

def pinca_de_fundo(df, p):
	name = 'Pinca_de_Fundo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = ((df['Low'].shift(abs(bar))==df['Low'].shift(1+abs(bar))) | \
			(df['Low'].shift(abs(bar))==df['Low'].shift(2+abs(bar))) | \
			(df['Low'].shift(abs(bar))==df['Low'].shift(3+abs(bar)))) & \
		(df['Low'].shift(abs(bar))<=df['Low'].rolling(window=3).min())

def pinca_de_topo(df, p):
	name = 'Pinca_de_Topo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = ((df['High'].shift(abs(bar))==df['High'].shift(1+abs(bar))) | \
			(df['High'].shift(abs(bar))==df['High'].shift(2+abs(bar))) | \
			(df['High'].shift(abs(bar))==df['High'].shift(3+abs(bar)))) & \
		(df['High'].shift(abs(bar)) >= (df['High'].rolling(window=3).max()))

def estrela_da_manha(df, p):
	name = 'Estrela_da_Manha('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))>df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(abs(bar))>df['Close'].shift(2+abs(bar))) & \
		(df['Close'].shift(2+abs(bar))<df['Open'].shift(2+abs(bar))) & \
		(df[['Close','Open']].max(axis=1).shift(1+abs(bar))<df['Close'].shift(2+abs(bar))) & \
		(df[['Close','Open']].max(axis=1).shift(1+abs(bar))<df['Open'].shift(abs(bar))) & \
		((df['Open'].shift(1+abs(bar))-df['Close'].shift(1+abs(bar)))<=((df['Open'].shift(2+abs(bar))-df['Close'].shift(2+abs(bar)))/4))

def estrela_da_tarde(df, p):
	name = 'Estrela_da_Tarde('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))<df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(abs(bar))<df['Close'].shift(2+abs(bar))) & \
		(df['Close'].shift(2+abs(bar))>df['Open'].shift(2+abs(bar))) & \
		(df[['Close','Open']].min(axis=1).shift(1+abs(bar))>df['Close'].shift(2+abs(bar))) & \
		(df[['Close','Open']].min(axis=1).shift(1+abs(bar))>df['Open'].shift(abs(bar))) & \
		((df['Open'].shift(1+abs(bar))-df['Close'].shift(1+abs(bar)))<=((df['Open'].shift(2+abs(bar))-df['Close'].shift(2+abs(bar)))/4))

def bebe_abandonado_de_fundo(df, p):
	name = 'Bebe_Abandonado_de_Fundo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))>df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(abs(bar))>df['Close'].shift(2+abs(bar))) & \
		(df['Close'].shift(2+abs(bar))<df['Open'].shift(2+abs(bar))) & \
		(df['High'].shift(1+abs(bar))<df['Low'].shift(2+abs(bar))) & \
		(df['High'].shift(1+abs(bar))<df['Low'].shift(abs(bar))) & \
		((df['Open'].shift(1+abs(bar))-df['Close'].shift(1+abs(bar)))<=((df['Open'].shift(2+abs(bar))-df['Close'].shift(2+abs(bar)))/4))

def bebe_abandonado_de_topo(df, p):
	name = 'Bebe_Abandonado_de_Topo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))<df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(abs(bar))<df['Close'].shift(2+abs(bar))) & \
		(df['Close'].shift(2+abs(bar))>df['Open'].shift(2+abs(bar))) & \
		(df['Low'].shift(1+abs(bar))>df['High'].shift(2+abs(bar))) & \
		(df['Low'].shift(1+abs(bar))>df['High'].shift(abs(bar))) & \
		((df['Open'].shift(1+abs(bar))-df['Close'].shift(1+abs(bar)))<=((df['Open'].shift(2+abs(bar))-df['Close'].shift(2+abs(bar)))/4))

def estrela_tripla_de_fundo(df, p):
	name = 'Estrela_Tripla_de_Fundo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))==df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(2+abs(bar))==df['Open'].shift(2+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))==df['Open'].shift(1+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))<df['Close'].shift(2+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))<df['Close'].shift(abs(bar)))

def estrela_tripla_de_topo(df, p):
	name = 'Estrela_Tripla_de_Topo('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = (df['Close'].shift(abs(bar))==df['Open'].shift(abs(bar))) & \
		(df['Close'].shift(2+abs(bar))==df['Open'].shift(2+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))==df['Open'].shift(1+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))>df['Close'].shift(2+abs(bar))) & \
		(df['Close'].shift(1+abs(bar))>df['Close'].shift(abs(bar)))  

#######
##GAP##
#######
def gap_true_alta(df, p):
	name = 'GAP_Verdadeiro_de_Alta('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = df['High'].shift(1+abs(bar)) < df['Low'].shift(abs(bar))

def gap_true_baixa(df, p):
	name = 'GAP_Verdadeiro_de_Baixa('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = df['Low'].shift(1+abs(bar)) > df['High'].shift(abs(bar))

def gap_fech_abert_alta(df, p):
	name = 'GAP_fechamento/abertura_de_Alta('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = df['Close'].shift(1+abs(bar)) < df['Open'].shift(abs(bar))

def gap_fech_abert_baixa(df, p):
	name = 'GAP_fechamento/abertura_de_Baixa('+p+')'

	bar = int(p.split(',')[0])

	if name not in df.columns: 
		df[name] = df['Close'].shift(1+abs(bar)) > df['Open'].shift(abs(bar))

###################
##MOVING AVERAGES##
###################
# def Close_menos_med(self, df, par):                
#     par = par.replace(')', '').replace('(', '')
#     name = 'F-M('+par+')'

#     par = int(p.split(',')[0])

#     df[name] = df['Close'] - df['Close'].rolling(center=False,window=par).mean()

#     return df, name
	
# one_moving_average_list
def fech_cruza_cima_med(df, p):
	name = 'Fechamento_cruza_para_cima_a_media('+p+')'        
	
	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])

	med = 'MA('+str(pMed)+')'       

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False,window=pMed).mean()
			
	if name not in df.columns:            
		df[name] = ((df['Close'].shift(abs(bar))-df[med].shift(abs(bar)))>0.) & ((df['Close'].shift(1+abs(bar))-df[med].shift(1+abs(bar)))<0.)

def fech_cruza_baixo_med(df, p):
	name = 'Fechamento_cruza_para_baixo_a_media('+p+')'        
	
	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])

	med = 'MA('+str(pMed)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = ((df['Close'].shift(abs(bar))-df[med].shift(abs(bar)))<0.) & ((df['Close'].shift(1+abs(bar))-df[med].shift(1+abs(bar)))>0.)

def fech_menos_media_maior(df, p):
	name = 'Fechamento_menos_media>=X('+p+')'        

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pX = float(p[2])

	med = 'MA('+str(pMed)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = (df['Close'].shift(abs(bar))-df[med].shift(abs(bar)))>=pX

def fech_menos_media_menor(df, p):
	name = 'Fechamento_menos_media<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pX = float(p[2])

	med = 'MA('+str(pMed)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = (df['Close'].shift(abs(bar))-df[med].shift(abs(bar)))<=pX

# two_moving_average_list
def med1_cruza_cima_med2(df, p):
	name = 'Media_1_cruza_para_cima_a_Media_2('+p+')'
	 
	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])

	med1 = 'MA('+str(pMed1)+')'
	med2 = 'MA('+str(pMed2)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].rolling(center=False,window=pMed1).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].rolling(center=False,window=pMed2).mean()

	if name not in df.columns:
		df[name] = ((df[med1].shift(abs(bar))-df[med2].shift(abs(bar)))>0.) & ((df[med1].shift(1+abs(bar))-df[med2].shift(1+abs(bar)))<0.)

def med1_cruza_baixo_med2(df, p):
	name = 'Media_1_cruza_para_baixo_a_Media_2('+p+')'
	
	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])

	med1 = 'MA('+str(pMed1)+')'
	med2 = 'MA('+str(pMed2)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].rolling(center=False,window=pMed1).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].rolling(center=False,window=pMed2).mean()

	if name not in df.columns:
		df[name] = ((df[med1].shift(abs(bar))-df[med2].shift(abs(bar)))<0.) & ((df[med1].shift(1+abs(bar))-df[med2].shift(1+abs(bar)))>0.)

def med1_menos_med2_maior(df, p):
	name = 'Media_1_menos_Media_2>=X('+p+')'
	
	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pX = float(p[3])

	med1 = 'MA('+str(pMed1)+')'
	med2 = 'MA('+str(pMed2)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].rolling(center=False,window=pMed1).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].rolling(center=False,window=pMed2).mean()

	if name not in df.columns:
		df[name] = (df[med1].shift(abs(bar)) - df[med2].shift(abs(bar))) >= pX

def med1_menos_med2_menor(df, p):
	name = 'Media_1_menos_Media_2<=X('+p+')'        
	
	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pX = float(p[3])

	med1 = 'MA('+pMed1+')'
	med2 = 'MA('+pMed2+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].rolling(center=False,window=pMed1).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].rolling(center=False,window=pMed2).mean()

	if name not in df.columns:
		df[name] = (df[med1].shift(abs(bar)) - df[med2].shift(abs(bar))) <= pX

###################
##BOLLINGER BANDS##
###################
# bollinger_list
def percentB_maior(df, p):
	name = 'Percent_B>=X('+p+')'		

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pFact = float(p[2])
	pX = float(p[3])

	med = 'MA('+str(pMed)+')'
	std = 'STD('+str(pMed)+')'
	bs = 'BS('+str(pMed)+','+str(pFact)+')'
	bi = 'BI('+str(pMed)+','+str(pFact)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False, window=pMed).mean()

	if std not in df.columns:
		df[std] = df['Close'].rolling(center=False, window=pMed).std(ddof=0)

	if bs not in df.columns:
		df[bs] = df[med] + (pFact * df[std])

	if bi not in df.columns:
		df[bi] = df[med] - (pFact * df[std])

	if name not in df.columns:
		df[name] = ( np.where(df[bs].shift(abs(bar))==df[bi].shift(abs(bar)), 50.0, \
			100*(df['Close'].shift(abs(bar))-df[bi].shift(abs(bar)))/(df[bs].shift(abs(bar))-df[bi].shift(abs(bar)))) ) >= pX

def percentB_menor(df, p):
	name = 'Percent_B<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pFact = float(p[2])
	pX = float(p[3])

	med = 'MA('+str(pMed)+')'
	std = 'STD('+str(pMed)+')'
	bs = 'BS('+str(pMed)+','+str(pFact)+')'
	bi = 'BI('+str(pMed)+','+str(pFact)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False, window=pMed).mean()

	if std not in df.columns:
		df[std] = df['Close'].rolling(center=False, window=pMed).std(ddof=0)

	if bs not in df.columns:
		df[bs] = df[med] + (pFact * df[std])

	if bi not in df.columns:
		df[bi] = df[med] - (pFact * df[std])

	if name not in df.columns:
		df[name] = ( np.where(df[bs].shift(abs(bar))==df[bi].shift(abs(bar)), 50.0, \
			100*(df['Close'].shift(abs(bar))-df[bi].shift(abs(bar)))/(df[bs].shift(abs(bar))-df[bi].shift(abs(bar)))) ) <= pX

def bwidth_maior(df, p):
	name = 'BandWidth>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pFact = float(p[2])
	pX = float(p[3])

	med = 'MA('+str(pMed)+')'
	std = 'STD('+str(pMed)+')'
	bs = 'BS('+str(pMed)+','+str(pFact)+')'
	bi = 'BI('+str(pMed)+','+str(pFact)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False, window=pMed).mean()

	if std not in df.columns:
		df[std] = df['Close'].rolling(center=False, window=pMed).std(ddof=0)

	if bs not in df.columns:
		df[bs] = df[med] + (pFact * df[std])

	if bi not in df.columns:
		df[bi] = df[med] - (pFact * df[std])

	if name not in df.columns:
		df[name] = (100*(df[bs].shift(abs(bar))-df[bi].shift(abs(bar)))/df[med].shift(abs(bar))) >= pX

def bwidth_menor(df, p):
	name = 'BandWidth<=X('+par+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pFact = float(p[2])
	pX = float(p[3])

	med = 'MA('+str(pMed)+')'
	std = 'STD('+str(pMed)+')'
	bs = 'BS('+str(pMed)+','+str(pFact)+')'
	bi = 'BI('+str(pMed)+','+str(pFact)+')'

	if med not in df.columns:
		df[med] = df['Close'].rolling(center=False, window=pMed).mean()

	if std not in df.columns:
		df[std] = df['Close'].rolling(center=False, window=pMed).std(ddof=0)

	if bs not in df.columns:
		df[bs] = df[med] + (pFact * df[std])

	if bi not in df.columns:
		df[bi] = df[med] - (pFact * df[std])

	if name not in df.columns:
		df[name] = (100*(df[bs].shift(abs(bar))-df[bi].shift(abs(bar)))/df[med].shift(abs(bar))) <= pX

########
##MACD##
########
# MACD_list
def macd_cruza_sinal_cima(df, p):
	name = 'MACD_cruza_SINAL_para_cima('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if name not in df.columns:
		df[name] = (df[macd].shift(abs(bar))>df[sinal].shift(abs(bar))) & (df[macd].shift(1+abs(bar))<df[sinal].shift(1+abs(bar)))

def macd_cruza_sinal_baixo(df, p):
	name = 'MACD_cruza_SINAL_para_baixo('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if name not in df.columns:
		df[name] = (df[macd].shift(abs(bar))<df[sinal].shift(abs(bar))) & (df[macd].shift(1+abs(bar))>df[sinal].shift(1+abs(bar)))

def macd_maior(df, p):
	name = 'MACD>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	# pSinal = int(p[3])
	pX = float(p[4])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	# sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if name not in df.columns:		
		df[name] = df[macd].shift(abs(bar)) >= pX

def macd_menor(df, p):
	name = 'MACD<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	# pSinal = int(p[3])
	pX = float(p[4])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	# sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if name not in df.columns:
		df[name] = df[macd].shift(abs(bar)) <= pX

def sinal_maior(df, p):
	name = 'SINAL>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])
	pX = float(p[4])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if name not in df.columns:
		df[name] = df[sinal].shift(abs(bar)) >= pX

def sinal_menor(self, df, par):
	name = 'SINAL<=X('+par+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])
	pX = float(p[4])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if name not in df.columns:
		df[name] = df[sinal].shift(abs(bar)) <= pX

def hist_macd_topo(df, p):
	name = 'Histograma_MACD_Topo('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'
	hist = 'HIST('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if hist not in df.columns:
		df[hist] = df[macd] - df[sinal]

	if name not in df.columns:
		df[name] = (df[hist].shift(1+abs(bar)) > df[hist].shift(abs(bar))) & (df[hist].shift(1+abs(bar)) > df[hist].shift(2+abs(bar)))

def hist_macd_fundo(df, p):
	name = 'Histograma_MACD_Fundo('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'
	hist = 'HIST('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if hist not in df.columns:
		df[hist] = df[macd] - df[sinal]

	if name not in df.columns:
		df[name] = (df[hist].shift(1+abs(bar)) < df[hist].shift(abs(bar))) & (df[hist].shift(1+abs(bar)) < df[hist].shift(2+abs(bar)))

def hist_macd_maior(df, p):
	name = 'Histograma_MACD>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])
	pX = float(p[4])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'
	hist = 'HIST('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if hist not in df.columns:
		df[hist] = df[macd] - df[sinal]

	if name not in df.columns:
		df[name] = df[hist].shift(abs(bar)) >= pX

def hist_macd_menor(df, p):
	name = 'Histograma_MACD<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pSinal = int(p[3])
	pX = float(p[4])

	med1 = 'MAexp('+str(pMed1)+')'
	med2 = 'MAexp('+str(pMed2)+')'
	macd = 'MACD('+str(pMed1)+','+str(pMed2)+')'
	sinal = 'SINAL('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'
	hist = 'HIST('+str(pMed1)+','+str(pMed2)+','+str(pSinal)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].ewm(span=pMed1, adjust=False).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].ewm(span=pMed2, adjust=False).mean()

	if macd not in df.columns:
		df[macd] =  df[med1] - df[med2]

	if sinal not in df.columns:
		df[sinal] = df[macd].ewm(span=pSinal, adjust=False).mean()

	if hist not in df.columns:
		df[hist] = df[macd] - df[sinal]

	if name not in df.columns:
		df[name] = df[hist].shift(abs(bar)) <= pX

###################################
##DIRECTIONAL MOVMENT INDEX - ADX##
###################################
def tr_dm(df):        
	dmpList=[]
	dmnList=[]
	trList=[]
	tr=0.0
	dmp=0.0
	dmn=0.0
	for i in range(0, df.index[-1]):
		if i<1:
			tr=0
			dmp=0
			dmn=0
		else:
			tr = max((df.loc[i, 'High']-df.loc[i, 'Low']),abs(df.loc[i, 'High']-df.loc[i-1, 'Close']),abs(df.loc[i, 'Low']-df.loc[i-1, 'Close']))
			if (df.loc[i, 'High']-df.loc[i-1, 'High'])>(df.loc[i-1, 'Low']-df.loc[i, 'Low']):
				dmp = max((df.loc[i, 'High']-df.loc[i-1, 'High']),0)
			else:
				dmp = 0
			if (df.loc[i-1, 'Low']-df.loc[i, 'Low'])>(df.loc[i, 'Low']-df.loc[i-1, 'Low']):
				dmn = max((df.loc[i-1, 'Low']-df.loc[i, 'Low']),0)
			else:
				dmn = 0
		if tr!=0:                
			dmpList.append(100*dmp/tr)
			dmnList.append(100*dmn/tr)
		else:
			dmpList.append(0)
			dmnList.append(0)
	return dmpList, dmnList

def DIP_cruza_cima_DIN(df, p):
	name = 'DIp_cruza_DIn_para_cima('+p+')'		

	p = p.split(',')
	bar = int(p[0])
	pAdx = int(p[1])

	dip = 'DIp('+str(pAdx)+')'
	din = 'DIn('+str(pAdx)+')'

	dmpList, dmnList = tr_dm(df)

	if dip not in df.columns:
		df[dip] = pd.Series(dmpList).ewm(span=pAdx, adjust=False).mean()

	if din not in df.columns:
		df[din] = pd.Series(dmnList).ewm(span=pAdx, adjust=False).mean()

	if name not in df.columns:
		df[name] = ( df[dip].shift(abs(bar))>df[din].shift(abs(bar)) ) & ( df[dip].shift(1+abs(bar))<df[din].shift(1+abs(bar)) )

def DIP_cruza_baixo_DIN(df, p):
	name = 'DIp_cruza_DIn_para_baixo('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pAdx = int(p[1])

	dip = 'DIp('+str(pAdx)+')'
	din = 'DIn('+str(pAdx)+')'

	dmpList, dmnList = tr_dm(df)

	if dip not in df.columns:
		df[dip] = pd.Series(dmpList).ewm(span=pAdx, adjust=False).mean()

	if din not in df.columns:
		df[din] = pd.Series(dmnList).ewm(span=pAdx, adjust=False).mean()

	if name not in df.columns:
		df[name] = ( df[dip].shift(abs(bar))<df[din].shift(abs(bar)) ) & ( df[dip].shift(1+abs(bar))>df[din].shift(1+abs(bar)) )

def DIP_menos_DIN_maior(df, p):
	name = 'DIp_menos_DIn>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pAdx = int(p[1])
	pX = float(p[2])

	dip = 'DIp('+str(pAdx)+')'
	din = 'DIn('+str(pAdx)+')'

	dmpList, dmnList = tr_dm(df)

	if dip not in df.columns:
		df[dip] = pd.Series(dmpList).ewm(span=pAdx, adjust=False).mean()

	if din not in df.columns:
		df[din] = pd.Series(dmnList).ewm(span=pAdx, adjust=False).mean()

	if name not in df.columns:
		df[name] = (df[dip].shift(abs(bar))-df[din].shift(abs(bar))) >= pX

def DIP_menos_DIN_menor(df, p):
	name = 'DIp_menos_DIn<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pAdx = int(p[1])
	pX = float(p[2])

	dip = 'DIp('+str(pAdx)+')'
	din = 'DIn('+str(pAdx)+')'

	dmpList, dmnList = tr_dm(df)

	if dip not in df.columns:
		df[dip] = pd.Series(dmpList).ewm(span=pAdx, adjust=False).mean()

	if din not in df.columns:
		df[din] = pd.Series(dmnList).ewm(span=pAdx, adjust=False).mean()

	if name not in df.columns:
		df[name] = (df[dip].shift(abs(bar))-df[din].shift(abs(bar))) <= pX

def ADX_maior(df, p):
	name = 'ADX>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pAdx = int(p[1])
	pX = float(p[2])

	dip = 'DIp('+str(pAdx)+')'
	din = 'DIn('+str(pAdx)+')'
	adx = 'ADX('+str(pAdx)+')'

	dmpList, dmnList = tr_dm(df)

	if dip not in df.columns:
		df[dip] = pd.Series(dmpList).ewm(span=pAdx, adjust=False).mean()

	if din not in df.columns:
		df[din] = pd.Series(dmnList).ewm(span=pAdx, adjust=False).mean()

	if adx not in df.columns:
		df[adx] = 100*abs(df[dip]-df[din])/(df[dip]+df[din])
		df[adx] = df[adx].ewm(span=pAdx, adjust=False).mean()

	if name not in df.columns:
		df[name] = df[adx].shift(abs(bar)) >= pX

def ADX_menor(df, p):
	name = 'ADX<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pAdx = int(p[1])
	pX = float(p[2])

	dip = 'DIp('+str(pAdx)+')'
	din = 'DIn('+str(pAdx)+')'
	adx = 'ADX('+str(pAdx)+')'

	dmpList, dmnList = tr_dm(df)

	if dip not in df.columns:
		df[dip] = pd.Series(dmpList).ewm(span=pAdx, adjust=False).mean()

	if din not in df.columns:
		df[din] = pd.Series(dmnList).ewm(span=pAdx, adjust=False).mean()

	if adx not in df.columns:
		df[adx] = 100*abs(df[dip]-df[din])/(df[dip]+df[din])
		df[adx] = df[adx].ewm(span=pAdx, adjust=False).mean()

	if name not in df.columns:
		df[name] = df[adx].shift(abs(bar)) <= pX
	
##############
##STOCHASTIC##
##############
def K_cruza_cima_D(df, p):
	name = 'K_cruza_D_para_cima('+p+')'		

	p = p.split(',')
	bar = int(p[0])
	pKF = int(p[1])
	pKS = int(p[2])
	pD = int(p[3])

	kf = 'Kf('+str(pKF)+')'
	ks = 'Ks('+str(pKF)+','+str(pKS)+')'
	ds = 'ds('+str(pKF)+','+str(pKS)+','+str(pD)+')'

	if kf not in df.columns:
		df[kf] = 100*(df['Close']-df['Low'].rolling(center=False,window=pKF).min())/(df['High'].rolling(center=False,window=pKF).max()-df['Low'].rolling(center=False,window=pKF).min())
		df[kf].replace([np.inf, -np.inf, ''], float(100), inplace=True)

	if ks not in df.columns:
		df[ks] = df[kf].rolling(center=False, window=pKS).mean()

	if ds not in df.columns:
		df[ds] = df[ks].rolling(center=False, window=pD).mean()

	if name not in df.columns:
		df[name] = ( df[ks].shift(abs(bar))>df[ds].shift(abs(bar)) ) & ( df[ks].shift(1+abs(bar))<df[ds].shift(1+abs(bar)) )

def K_cruza_baixo_D(df, p):
	name = 'K_cruza_D_para_baixo('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pKF = int(p[1])
	pKS = int(p[2])
	pD = int(p[3])

	kf = 'Kf('+str(pKF)+')'
	ks = 'Ks('+str(pKF)+','+str(pKS)+')'
	ds = 'ds('+str(pKF)+','+str(pKS)+','+str(pD)+')'

	if kf not in df.columns:
		df[kf] = 100*(df['Close']-df['Low'].rolling(center=False,window=pKF).min())/(df['High'].rolling(center=False,window=pKF).max()-df['Low'].rolling(center=False,window=pKF).min())
		df[kf].replace([np.inf, -np.inf, ''], float(100), inplace=True)

	if ks not in df.columns:
		df[ks] = df[kf].rolling(center=False, window=pKS).mean()

	if ds not in df.columns:
		df[ds] = df[ks].rolling(center=False, window=pD).mean()

	if name not in df.columns:
		df[name] = (df[ks].shift(abs(bar))<df[ds].shift(abs(bar))) & (df[ks].shift(1+abs(bar))>df[ds].shift(1+abs(bar)))

def K_maior(df, p):
	name = 'K>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pKF = int(p[1])
	pKS = int(p[2])
	pD = int(p[3])
	pX = float(p[4])

	kf = 'Kf('+str(pKF)+')'
	ks = 'Ks('+str(pKF)+','+str(pKS)+')'

	if kf not in df.columns:
		df[kf] = 100*(df['Close']-df['Low'].rolling(center=False,window=pKF).min())/(df['High'].rolling(center=False,window=pKF).max()-df['Low'].rolling(center=False,window=pKF).min())
		df[kf].replace([np.inf, -np.inf, ''], float(100), inplace=True)

	if ks not in df.columns:
		df[ks] = df[kf].rolling(center=False, window=pKS).mean()

	if name not in df.columns:
		df[name] = df[ks].shift(abs(bar))>=pX

def K_menor(df, p):
	name = 'K<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pKF = int(p[1])
	pKS = int(p[2])
	pD = int(p[3])
	pX = float(p[4])

	kf = 'Kf('+str(pKF)+')'
	ks = 'Ks('+str(pKF)+','+str(pKS)+')'

	if kf not in df.columns:
		df[kf] = 100*(df['Close']-df['Low'].rolling(center=False,window=pKF).min())/(df['High'].rolling(center=False,window=pKF).max()-df['Low'].rolling(center=False,window=pKF).min())
		df[kf].replace([np.inf, -np.inf, ''], float(100), inplace=True)

	if ks not in df.columns:
		df[ks] = df[kf].rolling(center=False, window=pKS).mean()

	if name not in df.columns:
		df[name] = df[ks].shift(abs(bar))<=pX

def D_maior(df, p):
	name = 'D>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pKF = int(p[1])
	pKS = int(p[2])
	pD = int(p[3])
	pX = float(p[4])

	kf = 'Kf('+str(pKF)+')'
	ks = 'Ks('+str(pKF)+','+str(pKS)+')'
	ds = 'ds('+str(pKF)+','+str(pKS)+','+str(pD)+')'

	if kf not in df.columns:
		df[kf] = 100*(df['Close']-df['Low'].rolling(center=False,window=pKF).min())/(df['High'].rolling(center=False,window=pKF).max()-df['Low'].rolling(center=False,window=pKF).min())
		df[kf].replace([np.inf, -np.inf, ''], float(100), inplace=True)

	if ks not in df.columns:
		df[ks] = df[kf].rolling(center=False, window=pKS).mean()

	if ds not in df.columns:
		df[ds] = df[ks].rolling(center=False, window=pD).mean()

	if name not in df.columns:
		df[name] = df[ds].shift(abs(bar))>=pX

def D_menor(df, p):
	name = 'D<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pKF = int(p[1])
	pKS = int(p[2])
	pD = int(p[3])
	pX = float(p[4])

	kf = 'Kf('+str(pKF)+')'
	ks = 'Ks('+str(pKF)+','+str(pKS)+')'
	ds = 'ds('+str(pKF)+','+str(pKS)+','+str(pD)+')'

	if kf not in df.columns:
		df[kf] = 100*(df['Close']-df['Low'].rolling(center=False,window=pKF).min())/(df['High'].rolling(center=False,window=pKF).max()-df['Low'].rolling(center=False,window=pKF).min())
		df[kf].replace([np.inf, -np.inf, ''], float(100), inplace=True)

	if ks not in df.columns:
		df[ks] = df[kf].rolling(center=False, window=pKS).mean()

	if ds not in df.columns:
		df[ds] = df[ks].rolling(center=False, window=pD).mean()

	if name not in df.columns:
		df[name] = df[ds].shift(abs(bar))<=pX

##########
##VOLUME##
##########
def vol_cruza_cima_med(df, p):
	name = 'Volume_cruza_media_para_cima('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])

	med = 'volMA('+str(pMed)+')'
	
	if med not in df.columns:
		df[med] = df['Volume'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = ( df['Volume'].shift(abs(bar))>df[med].shift(abs(bar)) ) & ( df['Volume'].shift(1+abs(bar))<df[med].shift(1+abs(bar)) )

def vol_cruza_baixo_med(df, p):
	name = 'Volume_cruza_media_para_baixo('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])

	med = 'volMA('+str(pMed)+')'
	
	if med not in df.columns:
		df[med] = df['Volume'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = (df['Volume'].shift(abs(bar))<df[med].shift(abs(bar))) & (df['Volume'].shift(1+abs(bar))>df[med].shift(1+abs(bar)))

def vol_menos_med_maior(df, p):
	name = 'Volume_menos_media>=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pX = float(p[2])

	med = 'volMA('+str(pMed)+')'
	
	if med not in df.columns:
		df[med] = df['Volume'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = (df['Volume'].shift(abs(bar))-df[med].shift(abs(bar))) >= pX

def vol_menos_med_menor(df, p):
	name = 'Volume_menos_media<=X('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed = int(p[1])
	pX = float(p[2])

	med = 'volMA('+str(pMed)+')'
	
	if med not in df.columns:
		df[med] = df['Volume'].rolling(center=False,window=pMed).mean()

	if name not in df.columns:
		df[name] = (df['Volume'].shift(abs(bar))-df[med].shift(abs(bar))) <= pX

###############
##Aleatoriedade
###############
def aleatoriedade(df, p):
	df['Inserir Aleatoriedade'] = pd.Series(np.random.choice([True, False], df.size))

##############
##DIDI INDEX##
##############
def didi_agulhada_compra(df, p):
	name = 'Agulhada_de_Compra('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pMed3 = int(p[3])

	med1 = 'MA('+str(pMed1)+')'
	med2 = 'MA('+str(pMed2)+')'
	med3 = 'MA('+str(pMed3)+')'

	dif12 = 'difMA('+str(pMed1)+','+str(pMed2)+')'
	dif32 = 'difMA('+str(pMed3)+','+str(pMed2)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].rolling(center=False,window=pMed1).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].rolling(center=False,window=pMed2).mean()

	if med3 not in df.columns:
		df[med3] = df['Close'].rolling(center=False,window=pMed3).mean()
	
	if dif12 not in df.columns:
		df[dif12] = df[med1]- df[med2]

	if dif32 not in df.columns:
		df[dif32] = df[med3]- df[med2]

	if name not in df.columns:
		df[name] = (df[dif12].shift(abs(bar))>0) & (df[dif32].shift(abs(bar))<0) & (df[dif12].shift(1+abs(bar))<0) & (df[dif32].shift(1+abs(bar))>0)

def didi_agulhada_venda(df, p):
	name = 'Agulhada_de_Venda('+p+')'

	p = p.split(',')
	bar = int(p[0])
	pMed1 = int(p[1])
	pMed2 = int(p[2])
	pMed3 = int(p[3])

	med1 = 'MA('+str(pMed1)+')'
	med2 = 'MA('+str(pMed2)+')'
	med3 = 'MA('+str(pMed3)+')'

	dif12 = 'difMA('+str(pMed1)+','+str(pMed2)+')'
	dif32 = 'difMA('+str(pMed3)+','+str(pMed2)+')'

	if med1 not in df.columns:
		df[med1] = df['Close'].rolling(center=False,window=pMed1).mean()

	if med2 not in df.columns:
		df[med2] = df['Close'].rolling(center=False,window=pMed2).mean()

	if med3 not in df.columns:
		df[med3] = df['Close'].rolling(center=False,window=pMed3).mean()
	
	if dif12 not in df.columns:
		df[dif12] = df[med1]- df[med2]

	if dif32 not in df.columns:
		df[dif32] = df[med3]- df[med2]

	if name not in df.columns:
		df[name] = (df[dif12].shift(abs(bar))<0) & (df[dif32].shift(abs(bar))>0) & (df[dif12].shift(1+abs(bar))>0) & (df[dif32].shift(1+abs(bar))<0)



functions_dict = {    #Candles
                      'Doji':doji, 'Martelo_Alta':martelo_alta,
                      'Martelo_Baixa':martelo_baixa,
                      'Martelo':martelo,
                      'Estrela_Cadente_Alta':estrela_cadente_alta,
                      'Estrela_Cadente_Baixa':estrela_cadente_baixa,
                      'Estrela_Cadente':estrela_cadente,
                      'Engolfo_de_Alta':engolfo_de_alta,
                      'Engolfo_de_Baixa':engolfo_de_baixa,
                      'Engolfo':engolfo, 
                      'Piercing_Line':piercing_line,
                      'Dark_Cloud_Cover':dark_cloud_cover,
                      'Harami_de_Fundo':harami_de_fundo,
                      'Harami_de_Topo':harami_de_topo,
                      'Ave_Migratoria_de_Fundo':ave_migratoria_de_fundo,
                      'Pinca_de_Fundo':pinca_de_fundo,
                      'Pinca_de_Topo':pinca_de_topo,
                      'Estrela_da_Manha':estrela_da_manha,
                      'Estrela_da_Tarde':estrela_da_tarde,
                      'Bebe_Abandonado_de_Fundo':bebe_abandonado_de_fundo,
                      'Bebe_Abandonado_de_Topo':bebe_abandonado_de_topo,
                      'Estrela_Tripla_de_Fundo':estrela_tripla_de_fundo,
                      'Estrela_Tripla_de_Topo':estrela_tripla_de_topo,
                      
                      # GAP
                      'GAP_Verdadeiro_de_Alta':gap_true_alta,
                      'GAP_Verdadeiro_de_Baixa':gap_true_baixa,
                      'GAP_fechamento/abertura_de_Alta':gap_fech_abert_alta,
                      'GAP_fechamento/abertura_de_Baixa':gap_fech_abert_baixa,

                      # Médias
                      'Fechamento_cruza_para_cima_a_media':fech_cruza_cima_med,
                      'Fechamento_cruza_para_baixo_a_media':fech_cruza_baixo_med,
                      'Fechamento_menos_media>=X':fech_menos_media_maior,
                      'Fechamento_menos_media<=X':fech_menos_media_menor,

                      'Media_1_cruza_para_cima_a_Media_2':med1_cruza_cima_med2,
                      'Media_1_cruza_para_baixo_a_Media_2':med1_cruza_baixo_med2,
                      'Media_1_menos_Media_2>=X':med1_menos_med2_maior,
                      'Media_1_menos_Media_2<=X':med1_menos_med2_menor,

                      # Agulhadas
                      'Agulhada_de_Compra':didi_agulhada_compra,
                      'Agulhada_de_Venda':didi_agulhada_venda,

                      # Bollinger
                      'Percent_B>=X':percentB_maior,
                      'Percent_B<=X':percentB_menor,
                      'BandWidth>=X':bwidth_maior,
                      'BandWidth<=X':bwidth_menor,

                      # MACD
                      'MACD_cruza_SINAL_para_cima':macd_cruza_sinal_cima,
                      'MACD_cruza_SINAL_para_baixo':macd_cruza_sinal_baixo,
                      'MACD>=X':macd_maior,
                      'MACD<=X':macd_menor,
                      'SINAL>=X':sinal_maior,
                      'SINAL<=X':sinal_menor,
                      'Histograma_MACD_Topo':hist_macd_topo,
                      'Histograma_MACD_Fundo':hist_macd_fundo,
                      'Histograma_MACD>=X':hist_macd_maior,
                      'Histograma_MACD<=X':hist_macd_menor,

                      # ADX
                      'DIp_cruza_DIn_para_cima':DIP_cruza_cima_DIN,
                      'DIp_cruza_DIn_para_baixo':DIP_cruza_baixo_DIN,
                      'DIp_menos_DIn>=X':DIP_menos_DIN_maior,
                      'DIp_menos_DIn<=X':DIP_menos_DIN_menor,
                      'ADX>=X':ADX_maior,
                      'ADX<=X':ADX_menor,

                      # Estocástico
                      'K_cruza_D_para_cima':K_cruza_cima_D,
                      'K_cruza_D_para_baixo':K_cruza_baixo_D,
                      'K>=X':K_maior,
                      'K<=X':K_menor,
                      'D>=X':D_maior,
                      'D<=X':D_menor,

                      # Volume
                      'Volume_cruza_media_para_cima':vol_cruza_cima_med,
                      'Volume_cruza_media_para_baixo':vol_cruza_baixo_med,
                      'Volume_menos_media>=X':vol_menos_med_maior,
                      'Volume_menos_media<=X':vol_menos_med_menor,
                      }