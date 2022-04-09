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

symbols = ['PETR4.SA','VALE3.SA','ITSA4.SA','MGLU3.SA','ITUB4.SA','AAPL','GOOG','AMZN','TSLA','^BVSP', '^DJI','^GSPC','^IXIC','BTC-USD','ETH-USD','DOGE-USD']
period = ['max','10y','5y','2y', '1y','ytd','6mo','3mo','1mo','1wk','5d','1d']
timeframe = ['1m','2m','5m','15m', '30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']

codec = ['Automático',
         'UTF-8','UTF-7','UTF-16','UTF-32',
         'ASCII',
         'latin_1','ISO-8859-1','ISO-8859-2',
         'ISO-8859-3','iso8859_4','iso8859_5',
         'iso8859_6','iso8859_7','iso8859_8',
         'iso8859_9','iso8859_10','iso8859_11',
         'iso8859_13','iso8859_14','iso8859_15',
         'iso8859_16'
         ]

delimiter = ['":"','";"','" "','"-"','"|"','","']

enter_prices = ['Entrar na abertura', 'Entrar no fechamento', 'Entrar na máxima', 'Entrar na mínima']
quit_prices = ['Sair no fechamento', 'Sair na abertura', 'Sair na máxima', 'Sair na mínima']

candles_list = ['Doji', 'Martelo_Alta', 'Martelo_Baixa', 'Martelo', 'Estrela_Cadente_Alta', 'Estrela_Cadente_Baixa', 'Estrela_Cadente', 
                'Engolfo_de_Alta', 'Engolfo_de_Baixa', 'Engolfo', 'Piercing_Line', 'Dark_Cloud_Cover', 'Harami_de_Fundo', 'Harami_de_Topo', 'Ave_Migratoria_de_Fundo',
                'Pinca_de_Fundo', 'Pinca_de_Topo', 'Estrela_da_Manha', 'Estrela_da_Tarde', 'Bebe_Abandonado_de_Fundo', 'Bebe_Abandonado_de_Topo', 
                'Estrela_Tripla_de_Fundo', 'Estrela_Tripla_de_Topo']

gap_list = ['GAP_Verdadeiro_de_Alta', 'GAP_Verdadeiro_de_Baixa', 'GAP_fechamento/abertura_de_Alta', 'GAP_fechamento/abertura_de_Baixa']

one_moving_average_list = ['Fechamento_cruza_para_cima_a_media', 'Fechamento_cruza_para_baixo_a_media', 'Fechamento_menos_media>=X', 'Fechamento_menos_media<=X']


two_moving_average_list = ['Media_1_cruza_para_cima_a_Media_2', 'Media_1_cruza_para_baixo_a_Media_2', 'Media_1_menos_Media_2>=X', 'Media_1_menos_Media_2<=X']

didi_list = ['Agulhada_de_Compra','Agulhada_de_Venda']

bollinger_list = ['Percent_B>=X', 'Percent_B<=X',
                   'BandWidth>=X', 'BandWidth<=X']

MACD_list = ['MACD_cruza_SINAL_para_cima', 'MACD_cruza_SINAL_para_baixo', 'MACD>=X', 'MACD<=X', 'SINAL>=X', 'SINAL<=X']

HistMACD_list= ['Histograma_MACD_Topo', 'Histograma_MACD_Fundo', 'Histograma_MACD>=X', 'Histograma_MACD<=X']

ADX_list = ['DIp_cruza_DIn_para_cima', 'DIp_cruza_DIn_para_baixo', 'DIp_menos_DIn>=X', 'DIp_menos_DIn<=X', 'ADX>=X', 'ADX<=X']

stocastic_list = ['K_cruza_D_para_cima', 'K_cruza_D_para_baixo', 'K>=X', 'K<=X', 'D>=X', 'D<=X']

volume_list = ['Volume_cruza_media_para_cima', 'Volume_cruza_media_para_baixo', 'Volume_menos_media>=X', 'Volume_menos_media<=X']

all_signals = candles_list + gap_list + one_moving_average_list + two_moving_average_list + didi_list + bollinger_list + MACD_list + HistMACD_list + ADX_list + stocastic_list + volume_list


# functions_dict = {    #Candles
#                       'Doji':'doji', 'Martelo_Alta':'martelo_alta',
#                       'Martelo_Baixa':'martelo_baixa',
#                       'Martelo':'martelo',
#                       'Estrela_Cadente_Alta':'estrela_cadente_alta',
#                       'Estrela_Cadente_Baixa':'estrela_cadente_baixa',
#                       'Estrela_Cadente':'estrela_cadente',
#                       'Engolfo_de_Alta':'engolfo_de_alta',
#                       'Engolfo_de_Baixa':'engolfo_de_baixa',
#                       'Engolfo':'engolfo', 
#                       'Piercing_Line':'piercing_line',
#                       'Dark_Cloud_Cover':'dark_cloud_cover',
#                       'Harami_de_Fundo':'harami_de_fundo',
#                       'Harami_de_Topo':'harami_de_topo',
#                       'Ave_Migratoria_de_Fundo':'ave_migratoria_de_fundo',
#                       'Pinca_de_Fundo':'pinca_de_fundo',
#                       'Pinca_de_Topo':'pinca_de_topo',
#                       'Estrela_da_Manha':'estrela_da_manha',
#                       'Estrela_da_Tarde':'estrela_da_tarde',
#                       'Bebe_Abandonado_de_Fundo':'bebe_abandonado_de_fundo',
#                       'Bebe_Abandonado_de_Topo':'bebe_abandonado_de_topo',
#                       'Estrela_Tripla_de_Fundo':'estrela_tripla_de_fundo',
#                       'Estrela_Tripla_de_Topo':'estrela_tripla_de_topo',
                      
#                       # GAP
#                       'GAP_Verdadeiro_de_Alta':'gap_true_alta',
#                       'GAP_Verdadeiro_de_Baixa':'gap_true_baixa',
#                       'GAP_fechamento/abertura_de_Alta':'gap_fech_abert_alta',
#                       'GAP_fechamento/abertura_de_Baixa':'gap_fech_abert_baixa',

#                       # Médias
#                       'Fechamento_cruza_para_cima_a_media':'fech_cruza_cima_med',
#                       'Fechamento_cruza_para_baixo_a_media':'fech_cruza_baixo_med',
#                       'Fechamento_menos_media>=X':'fech_menos_media_maior',
#                       'Fechamento_menos_media<=X':'fech_menos_media_menor',

#                       'Media_1_cruza_para_cima_a_Media_2':'med1_cruza_cima_med2',
#                       'Media_1_cruza_para_baixo_a_Media_2':'med1_cruza_baixo_med2',
#                       'Media_1_menos_Media_2>=X':'med1_menos_med2_maior',
#                       'Media_1_menos_Media_2<=X':'med1_menos_med2_menor',

#                       # Agulhadas
#                       'Agulhada_de_Compra':'didi_agulhada_compra',
#                       'Agulhada_de_Venda':'didi_agulhada_venda',

#                       # Bollinger
#                       'Percent_B>=X':'percentB_maior',
#                       'Percent_B<=X':'percentB_menor',
#                       'BandWidth>=X':'bwidth_maior',
#                       'BandWidth<=X':'bwidth_menor',

#                       # MACD
#                       'MACD_cruza_SINAL_para_cima':'macd_cruza_sinal_cima',
#                       'MACD_cruza_SINAL_para_baixo':'macd_cruza_sinal_baixo',
#                       'MACD>=X':'macd_maior',
#                       'MACD<=X':'macd_menor',
#                       'SINAL>=X':'sinal_maior',
#                       'SINAL<=X':'sinal_menor',
#                       'Histograma_MACD_Topo':'hist_macd_topo',
#                       'Histograma_MACD_Fundo':'hist_macd_fundo',
#                       'Histograma_MACD>=X':'hist_macd_maior',
#                       'Histograma_MACD<=X':'hist_macd_menor',

#                       # ADX
#                       'DIp_cruza_DIn_para_cima':'DIP_cruza_cima_DIN',
#                       'DIp_cruza_DIn_para_baixo':'DIP_cruza_baixo_DIN',
#                       'DIp_menos_DIn>=X':'DIP_menos_DIN_maior',
#                       'DIp_menos_DIn<=X':'DIP_menos_DIN_menor',
#                       'ADX>=X':'ADX_maior',
#                       'ADX<=X':'ADX_menor',

#                       # Estocástico
#                       'K_cruza_D_para_cima':'K_cruza_cima_D',
#                       'K_cruza_D_para_baixo':'K_cruza_baixo_D',
#                       'K>=X':'K_maior',
#                       'K<=X':'K_menor',
#                       'D>=X':'D_maior',
#                       'D<=X':'D_menor',

#                       # Volume
#                       'Volume_cruza_media_para_cima':'vol_cruza_cima_med',
#                       'Volume_cruza_media_para_baixo':'vol_cruza_baixo_med',
#                       'Volume_menos_media>=X':'vol_menos_med_maior',
#                       'Volume_menos_media<=X':'vol_menos_med_menor',                      
#                       }









l = ['--Candlesticks--', 'Doji', 'Martelo Alta', 'Martelo Baixa', 'Martelo', 'Estrela Cadente Alta', 'Estrela Cadente Baixa', 'Estrela Cadente', 'Engolfo de Alta',
'Engolfo de Baixa', 'Engolfo', 'Piercing Line', 'Dark Cloud Cover', 'Harami de Fundo', 'Harami de Topo', 'Pinça de Fundo', 'Pinça de Topo', 'Estrela da Manhã',
'Estrela da Tarde', 'Bebê Abandonado de Fundo', 'Bebê Abandonado de Topo', 'Estrela Tripla de Fundo', 'Estrela Tripla de Topo', '--GAPS--', 'GAP Verdadeiro de Alta',
'GAP Verdadeiro de Baixa', 'GAP - fechamento/abertura de Alta', 'GAP - fechamento/abertura de Baixa', '--Médias Móveis--', 'Fechamento cruza para cima a média',
'Fechamento cruza para baixo a média', 'Fechamento menos média >= X', 'Fechamento menos média <= X', 'Média_1 cruza para cima a Média_2', 'Média_1 cruza para baixo a Média_2',
'Média_1 menos Média_2 >= X', 'Média_1 menos Média_2 <= X', '--Didi Index--', 'Agulhada de Compra', 'Agulhada de Venda', '--Bollinger--', 'Percent B >= X', 'Percent B <= X',
'BandWidth >= X', 'BandWidth <= X', '--MACD--', 'MACD cruza SINAL para cima', 'MACD cruza SINAL para baixo', 'MACD >= X', 'MACD <= X', 'SINAL >= X', 'SINAL <= X', '--Histograma MACD--', 
'Histograma MACD Topo', 'Histograma MACD Fundo', 'Histograma MACD >= X', 'Histograma MACD <= X', '--ADX--', 'DIp cruza DIn para cima', 'DIp cruza DIn para baixo', 'DIp menos DIn >= X', 
'DIp menos DIn <= X', 'ADX >= X', 'ADX <= X', '--Estocástico Lento--', 'K cruza D para cima', 'K cruza D para baixo', 'K >= X', 'K <= X', 'D >= X', 'D <= X', '--Volume--', 
'Volume cruza média para cima', 'Volume cruza média para baixo', 'Volume menos média >= X', 'Volume menos média <= X']

# print(dict(zip([b for b in l if '--' not in b], all_signals)))


# binsHist = ['Automático', 'Definir Inteiro', 'Freedman Diaconis',
#             'Doane', 'Scott', 'Rice', 'Sturges', 'Raíz Quadrada']

# tipo_op_cv = ['Compra', 'Venda']
# tipo_op_dtn = ['Day Trade','Normal']
# dict_col_arq = {'Data':'self.data', 'Hora':'self.hora', 'Abertura':'self.abertura',
#                    'Máxima':'self.maximo', 'Mínima':'self.minimo', 'Fechamento':'self.fechamento',
#                    'Papéis':'self.papeis', 'Negócios':'self.negocios', 'Financeiro':'self.financeiro','--Vazio--':''}

# dict_col_arq_afuncoes2 = {'Data':'self.data.append(d)', 'Hora':'self.hora.append(h)', 'Abertura':'self.abertura.append(a)',
#                    'Máxima':'self.maximo.append(ma)', 'Mínima':'self.minimo.append(mi)', 'Fechamento':'self.fechamento.append(f)',
#                    'Papéis':'self.papeis.append(p)', 'Negócios':'self.negocios.append(n)', 'Financeiro':'self.financeiro.append(fin)','--Vazio--':''}

# dict_col_arq_bfuncoes2 = {'Data':'d', 'Hora':'h', 'Abertura':'a',
#                    'Máxima':'ma', 'Mínima':'mi', 'Fechamento':'f',
#                    'Papéis':'p', 'Negócios':'n', 'Financeiro':'fin','--Vazio--':''}

# colunas_arquivo = ['Data', 'Hora', 'Abertura', 'Máxima', 'Mínima', 'Fechamento', 'Negócios', 'Papéis', 'Financeiro','--Vazio--']

# formato_data = ['dd/mm/aaaa', 'dd-mm-aaaa', 'dd.mm.aaaa',
#                  'mm/dd/aaaa', 'mm-dd-aaaa', 'mm.dd.aaaa',
#                  'aaaa/mm/dd', 'aaaa-mm-dd', 'aaaa.mm.dd']

# metodoTopoFundo = ['Tradicional', 'Regressão Linear']
# precoTopoFundo = ['Máximas e Mínimas', 'Fechamento', 'Preço Médio']
# limitador_arquivo = ['Delimitador', '","','":"','";"','" "','"-"','"|"']


# valor_numerico=['Valor Numérico']

# precos_lista = ['Abertura', 'Máxima', 'Mínima','Fechamento',
#                 'Preço Médio (máxima e mínima)','Preço Médio (abertura e fechamento)',
#                 ]









##                   'Banda de Bollinger-Superior','Banda de Bollinger-Inferior',
##                   'Banda de Bollinger-Média',
##                   'Fechamento acima da banda superior',
##                   'Fechamento abaixo da banda superior',
##                   'Fechamento cruza banda superior para cima',
##                   'Fechamento cruza banda superior para baixo',
##                   'Fechamento acima da banda inferior',
##                   'Fechamento abaixo da banda inferior',
##                   'Fechamento cruza banda inferior para cima',
##                   'Fechamento cruza banda inferior para baixo',
##                   ]

#, 'Banda de Bollinger-Width','Banda de Bollinger-%b']


##              'Didi Index Aviso de Compra','Didi Index Aviso de Venda',]



stop_lista = ['--Stop pré-definido--', 'Stop Gain', 'Stop Loss']

##              'Desvalorização Máxima: Entrada vs Fechamento',
##              'Desvalorização Máxima: Entrada vs Abertura', 'Desvalorização Máxima: Entrada vs Máxima',
##              'Desvalorização Máxima: Entrada vs Mínima','Valorização Máxima: Entrada vs Fechamento',
##              'Valorização Máxima: Entrada vs Abertura', 'Valorização Máxima: Entrada vs Máxima',
##              'Valorização Máxima: Entrada vs Mínima']



aleat = ['--Aleatoriedade--', 'Inserir Aleatoriedade']

# estudos_estatisticos_diap = precos_lista + candles_lista + gap_lista# + volume_lista[1:2]

# estudos_estatisticos_1p = valor_numerico + media_movel_lista[1:-2]# + volume_lista[2:]

# estudos_estatisticos_2p =  media_movel_lista[4:]

##estudos_estatisticos_3p = ['Agulhada de Compra Didi Index','Agulhada de Venda Didi Index',
##                           'Aviso de Compra Didi Index', 'Aviso de Venda Didi Index']

##estudos_estatisticos = estudos_estatisticos_0p + estudos_estatisticos_1p + estudos_estatisticos_2p + estudos_estatisticos_3p

##estudos_lista = valor_numerico + precos_lista + candles_lista + gap_lista + volume_lista + media_movel_lista + bollinger_lista + didi_lista + estocastico_lista#estudos_estatisticos
##estudos_lista = valor_numerico + precos_lista + candles_lista + gap_lista + media_movel_lista + didi_lista + bollinger_lista + ADX_lista + estocastico_lista + volume_lista
# estudos_lista = candles_lista + gap_lista + media_movel_lista + didi_lista + bollinger_lista + MACD_lista + HistMACD_lista + ADX_lista + estocastico_lista + volume_lista + aleat

condicional_lista = ['E (and)', 'Ou (or)']#, 'Igual a (=)', 'Diferente de (!=)', 'Maior que (>)',
##                 'Menor que (<)', 'Maior ou Igual a (>=)', 'Menor ou Igual a (<=)']

dict_histBins = {'Automático':'auto', 'Freedman Diaconis':'fd',
                 'Doane':'doane', 'Scott':'scott', 'Rice':'rice',
                 'Sturges':'sturges', 'Raíz Quadrada':'sqrt'}

dict_condicional_lista = {'Condicional 1':'','Condicional 2':'','Condicional 3':'',
                     'Condicional 4':'','Condicional 5':'',
                          'E (and)':'(E)', 'Ou (or)':'(Ou)', 'Igual a (=)':'(=)', 'Diferente de (!=)':'(!=)',
                          'Maior que (>)':'(>)', 'Menor que (<)':'(&#x3c;)', 'Maior ou Igual a (>=)':'(>=)', 'Menor ou Igual a (<=)':'(&#x3c;=)'}

dicionario_sinais = {'Condicional 1':'','Condicional 2':'','Condicional 3':'',
                     'Condicional 4':'','Condicional 5':'',
                     'E (and)' : " & ", 'Ou (or)' : " | ",
                     'Igual a (=)' : '==', 'Diferente de (!=)' : '!=', 'Maior que (>)' : '>',
                     'Menor que (<)' : '<','Maior ou Igual a (>=)' : '>=',
                     'Menor ou Igual a (<=)' : '<=',
                     }

##INSERIR FUNÇÕES PARA SAÍDA STOP COMO VALORIZAÇÃO/DESVALORIZAÇÃO DO DIA ENTRADA, ACIMA DA MINIMA/MAXIMA ETC....
dicionario_funcoes = {'Sinal 1':'','Sinal 2':'','Sinal 3':'','Sinal 4':'','Sinal 5':'',
##                      'Valor Numérico': 'self.modfunc.valor_numerico(total',
##                      'Abertura':'self.modfunc.preco_abertura(total',
##                      'Máxima':'self.modfunc.preco_maximo(total',
##                      'Mínima':'self.modfunc.preco_minimo(total',
##                      'Fechamento':'self.modfunc.preco_fechamento(total',
##                      'Preço Médio (máxima e mínima)':'self.modfunc.precomedio_max_min(total',
##                      'Preço Médio (abertura e fechamento)':'self.modfunc.precomedio_aber_fech(total',
                      #
                      'Doji':'self.modfunc.doji(inicio,fim', 'Martelo Alta':'self.modfunc.martelo_alta(inicio,fim',
                      'Martelo Baixa':'self.modfunc.martelo_baixa(inicio,fim',
                      'Martelo':'self.modfunc.martelo(inicio,fim',
                      'Estrela Cadente Alta':'self.modfunc.estrela_cadente_alta(inicio, fim',
                      'Estrela Cadente Baixa':'self.modfunc.estrela_cadente_baixa(inicio, fim',
                      'Estrela Cadente':'self.modfunc.estrela_cadente(inicio, fim',
                      'Engolfo de Alta':'self.modfunc.engolfo_de_alta(inicio, fim',
                      'Engolfo de Baixa':'self.modfunc.engolfo_de_baixa(inicio, fim',
                      'Engolfo':'self.modfunc.engolfo(inicio, fim', 
                      'Piercing Line':'self.modfunc.piercing_line(inicio, fim',
                      'Dark Cloud Cover':'self.modfunc.dark_cloud_cover(inicio, fim',
                      'Harami de Fundo':'self.modfunc.harami_de_fundo(inicio, fim',
                      'Harami de Topo':'self.modfunc.harami_de_topo(inicio, fim',
                      'Ave Migratória':'self.modfunc.ave_migratoria(inicio, fim',
                      'Pinça de Fundo':'self.modfunc.pinca_de_fundo(inicio, fim',
                      'Pinça de Topo':'self.modfunc.pinca_de_topo(inicio, fim',
                      'Estrela da Manhã':'self.modfunc.estrela_da_manha(inicio, fim',
                      'Estrela da Tarde':'self.modfunc.estrela_da_tarde(inicio, fim',
                      'Bebê Abandonado de Fundo':'self.modfunc.bebe_abandonado_de_fundo(inicio, fim',
                      'Bebê Abandonado de Topo':'self.modfunc.bebe_abandonado_de_topo(inicio, fim',
                      'Estrela Tripla de Fundo':'self.modfunc.estrela_tripla_de_fundo(inicio, fim',
                      'Estrela Tripla de Topo':'self.modfunc.estrela_tripla_de_topo(inicio, fim',
                      #
                      'GAP Verdadeiro de Alta':'self.modfunc.gap_true_alta(inicio, fim',
                      'GAP Verdadeiro de Baixa':'self.modfunc.gap_true_baixa(inicio, fim',
                      'GAP - fechamento/abertura de Alta':'self.modfunc.gap_fech_abert_alta(inicio, fim',
                      'GAP - fechamento/abertura de Baixa':'self.modfunc.gap_fech_abert_baixa(inicio, fim',
                      #
##                      'Média Aritmética':'self.modfunc.media_aritmetica(total',
                      'Fechamento cruza para cima a média':'self.modfunc.fech_cruza_cima_med(inicio, fim',
                      'Fechamento cruza para baixo a média':'self.modfunc.fech_cruza_baixo_med(inicio, fim',
                      'Fechamento acima da média':'self.modfunc.fech_acima_med(inicio, fim',
                      'Fechamento abaixo da média':'self.modfunc.fech_abaixo_med(inicio, fim',
                      'Média_1 cruza para cima a Média_2':'self.modfunc.med1_cruza_cima_med2(inicio, fim',
                      'Média_1 cruza para baixo a Média_2':'self.modfunc.med1_cruza_baixo_med2(inicio, fim',
                      'Média_1 acima da Média_2':'self.modfunc.med1_acima_med2(inicio, fim',
                      'Média_1 abaixo da Média_2':'self.modfunc.med1_abaixo_med2(inicio, fim',
                      #
                      'Didi Index Agulhada de Compra':'self.modfunc.didi_agulhada_compra(inicio, fim',
                      'Didi Index Agulhada de Venda':'self.modfunc.didi_agulhada_venda(inicio, fim',
                      'Didi Index Aviso de Compra':'self.modfunc.didi_aviso_compra(inicio, fim',
                      'Didi Index Aviso de Venda':'self.modfunc.didi_aviso_venda(inicio, fim',
                      #Bollinger
                      'Fechamento acima da banda superior':'self.modfunc.fech_acima_bollinger_sup(inicio, fim',
                      'Fechamento abaixo da banda superior':'self.modfunc.fech_abaixo_bollinger_sup(inicio, fim',
                      'Fechamento cruza banda superior para cima':'self.modfunc.fech_cruza_cima_bollinger_sup(inicio, fim',
                      'Fechamento cruza banda superior para baixo':'self.modfunc.fech_cruza_baixo_bollinger_sup(inicio, fim',
                      'Fechamento acima da banda inferior':'self.modfunc.fech_acima_bollinger_inf(inicio, fim',
                      'Fechamento abaixo da banda inferior':'self.modfunc.fech_abaixo_bollinger_inf(inicio, fim',
                      'Fechamento cruza banda inferior para cima':'self.modfunc.fech_cruza_cima_bollinger_inf(inicio, fim',
                      'Fechamento cruza banda inferior para baixo':'self.modfunc.fech_cruza_baixo_bollinger_inf(inicio, fim',
                      
##                      'B.Bollinger Sup.':'self.modfunc.bollinger_superior(total',
##                      'B.Bollinger Inf.':'self.modfunc.bollinger_inferior(total',
##                      'B.Bollinger Interm.':'self.modfunc.bollinger_media(total',
                      #
                      '+DI acima de -DI':'self.modfunc.DIP_acima_DIN(inicio,fim',
                      '+DI abaixo de -DI':'self.modfunc.DIP_abaixo_DIN(inicio,fim',
                      '+DI cruza -DI para cima':'self.modfunc.DIP_cruza_cima_DIN(inicio,fim',
                      '+DI cruza -DI para baixo':'self.modfunc.DIP_cruza_baixo_DIN(inicio,fim',
                      'ADX maior ou igual a X':'self.modfunc.ADX_maior_Valor(inicio,fim',
                      'ADX menor ou igual a X':'self.modfunc.ADX_menor_Valor(inicio,fim',
                      #
                      'Estocástico - K cruza de baixo para cima D':'self.modfunc.estocastico_lento_cruzamento_compra(inicio, fim',
                      'Estocástico - K cruza de cima para baixo D':'self.modfunc.estocastico_lento_cruzamento_venda(inicio, fim',
                      'Estocástico - K cruza para cima VALOR':'self.modfunc.estocK_lento_cruza_cima_limite(inicio, fim',
                      'Estocástico - K cruza para baixo VALOR':'self.modfunc.estocK_lento_cruza_baixo_limite(inicio, fim',
                      'Estocástico - D cruza para cima VALOR':'self.modfunc.estocD_lento_cruza_cima_limite(inicio, fim',
                      'Estocástico - D cruza para baixo VALOR':'self.modfunc.estocD_lento_cruza_baixo_limite(inicio, fim',
                      #
##                      'Volume':'self.modfunc.volume(total',
##                      'Média Volume':'self.modfunc.med_volume(total',
                      'Volume acima da média':'self.modfunc.volume_acima_med(inicio, fim',
                      'Volume abaixo da média':'self.modfunc.volume_abaixo_med(inicio, fim',
                      'Volume cruza para cima a média':'self.modfunc.volume_cruza_cima_med(inicio, fim',
                      'Volume cruza para baixo a média':'self.modfunc.volume_cruza_baixo_med(inicio, fim',
                      #
                      'Inserir Aleatoriedade':'self.modfunc.aleatoriedade(inicio, fim',
                      #
                      'Entrar na abertura':'self.modfunc.abertura[total+k]',
                      'Entrar na máxima':'self.modfunc.maximo[total+k]',
                      'Entrar na mínima':'self.modfunc.minimo[total+k]',
                      'Entrar no fechamento':'self.modfunc.fechamento[total+k]',
                      #
                      'Sair na abertura':'self.modfunc.abertura[total+k]',
                      'Sair na máxima':'self.modfunc.maximo[total+k]',
                      'Sair na mínima':'self.modfunc.minimo[total+k]',
                      'Sair no fechamento':'self.modfunc.fechamento[total+k]',
                      #
                      'SL - Varição em Pontos':'self.modfunc.stopLossPontos(total+k, comprado_vendido, preco_ref, slvar)',
                      'SL - Varição Percentual':'self.modfunc.stopLossPercentual(total+k, comprado_vendido, preco_ref, slvar)',
                      'TP - Varição em Pontos':'self.modfunc.takeProfitPontos(total+k, comprado_vendido, preco_ref, tpvar)',
                      'TP - Varição Percentual':'self.modfunc.takeProfitPercentual(total+k, comprado_vendido, preco_ref, tpvar)'
                      }




