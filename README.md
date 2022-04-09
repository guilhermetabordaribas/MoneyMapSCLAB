# SCLAB MoneyMap 6.0

MoneyMap é um calculador de backtest, programado em Python, para estudo e pesquisa em análise técnica para ativos financeiros, como ações, opções, índices, moedas e cryptos.
Com ele é possível gerar combinações de estratégias de análise técnica sem programar nada, apenas inserindo o setup.

Este programa ainda está em sua versão BETA de testes, portanto, não deve ser usado como fonte única de resultados de eficiência, uma vez que ainda está em fase de desenvolvimento e pode conter erros. 

Caso você queira usar apenas os arquivos executáveis, basta baixá-los nos links abaixo:
* [MoneyMapSCLAB para Windows 10](https://drive.google.com/file/d/1IQobdoLuFY0hmuRhJaSLaKg8KFWz8xc9/view?usp=sharing)
* [MoneyMapSCLAB para Ubuntu 20.04](https://drive.google.com/file/d/17yKLS8MPUoofjoaUPsFFmtBVWXk3UjLa/view?usp=sharing)

Caso seja inciante em Python e queira baixar os arquivos e começar a mexer nos códigos fonte, visite a [Wiki](https://github.com/guilhermetabordaribas/MoneyMapSCLAB/wiki) deste projeto. Fique à vontade para sugerir melhorias e pull requests.

---
##### **ATENÇÃO:** É muito importante lembrar que os resultados de eficiência são destinados ao estudo da análise gráfica, com único intuito de qualificar os indicadores e suas estratégias, de forma alguma destina-se a indicar ou influenciar uma compra ou uma venda específica. Existem profissionais certificados que (de acordo com a Instrução CVM 483) são autorizados a emitir relatórios que, expressamente, indicam uma compra ou uma venda de determinado ativo num determinado tempo. Este não é o nosso papel. Portanto, lembre-se, se estiver procurado indicações de preços/ações/volumes para a entrada/abertura/fechamento de alguma operação, ou, gerenciamento de posições, procure sempre um profissional cetificado pela APIMEC, não se deixe influenciar por qualquer profissional.
---


Este programa é feito integralmente em Python 3.8 e pacotes desta mesma linguagem.
* matplotlib==3.4.3
* numpy==1.21.2
* pandas==1.3.2
* Pillow==9.0.1
* scipy==1.7.1
* seaborn==0.11.2
* ttkbootstrap==0.5.1
* yfinance==0.1.63

Como este programa utiliza o pacote yfinance, o qual utiliza API Yahoo!, Y!Finance, e Yahoo! finance registradas sob a marca Yahoo, Inc.  Deve-se ressaltar que a iniciativa Sclab não é afiliada, endosada ou verificada pela Yahoo, Inc. Este programa é uma ferramenta de código aberto que usa APIs disponíveis publicamente do Yahoo e se destina a fins edicacionais e de pesquisa.
Você deve consultar os termos de uso do Yahoo! [aqui](https://policies.yahoo.com/us/en/yahoo/terms/product-atos/apiforydn/index.htm), [aqui](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html) e [aqui](https://policies.yahoo.com/us/en/yahoo/terms/index.htm)
