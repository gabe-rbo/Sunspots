"""
Sites:
https://www.sidc.be/SILSO/datafiles

Usar pandas IO tools
Aqui contém rascunhos e testes para as funções que serão passadas para o notebook, também estão aqui as instruções
detalhadas de como cada etapa foi realizada.
"""

import pandas as pd
import numpy as np

"""
Para fazermos as análises dos arquivos mais facilmente, utilizaremos tabelas CSV (comma separated values), juntamente
à biblioteca pandas, importada como pd.
"""

# TSN = Total Sunspot Number
TSN_diario = pd.read_csv(r"C:\Users\gabri\PycharmProjects\ProgramacaoDeComputadores\TrabalhoPraticoManchasSolares\Dados\Total_sunspot_number\SN_d_tot_V2.0.csv", sep=';')
TSN_mensal_normal = pd.read_csv(r"C:\Users\gabri\PycharmProjects\ProgramacaoDeComputadores\TrabalhoPraticoManchasSolares\Dados\Total_sunspot_number\SN_m_tot_V2.0.csv", sep=';')
TSN_mensal_suavizado = pd.read_csv(r"C:\Users\gabri\PycharmProjects\ProgramacaoDeComputadores\TrabalhoPraticoManchasSolares\Dados\Total_sunspot_number\SN_ms_tot_V2.0.csv", sep=';')
TSN_anual = pd.read_csv(r"C:\Users\gabri\PycharmProjects\ProgramacaoDeComputadores\TrabalhoPraticoManchasSolares\Dados\Total_sunspot_number\SN_y_tot_V2.0.csv", sep=';')

"""
Tendo os arquivos lidos, precisamos analisá-los.
Suas informações serão salvas como dicionários. Para isso, leremos cada linha como uma tupla.

As seguintes informações derivam do site da SILSO:

---Em TSN_diario, as colunas simbolizam
Coluna de 1-3: Data no calendário gregoriano 
- Ano
- Mês
- Dia
Coluna 4: Data em fração de ano.
Coluna 5: Total diário de manchas solares. Um valor de -1 indica que não há dados para aquele dia (missing value).
Coluna 6: Desvio padrão diário da entrada da quantidade de manchas solares inseridas pelas estações individuais.
Coluna 7: Número de observações usadas para computar o total diário (coluna 5).
Coluna 8: Indicador de valor definitivo ou provisório. '1' indica que o valor é definitivo. '0' indica que o valor ainda é provisório.

---Em TSN_mensal_normal, as colunas simbolizam:
Coluna de 1-2: Data no calendário gregoriano 
- Ano
- Mês
Coluna 3: Data em fração de ano.
Coluna 4: Total mensal de manchas solares. Um valor de -1 indica que não há dados para aquele dia (missing value).
Coluna 5: Desvio padrão mensal da entrada da quantidade de manchas solares inseridas pelas estações individuais.
Coluna 6: Número de observações usadas para computar o total diário (coluna 5).
Coluna 7: Indicador de valor definitivo ou provisório. '1' indica que o valor é definitivo. '0' indica que o valor ainda é provisório.

---Em TSN_mensal_suavizado, as colunas  simbolizam:
Coluna de 1-2: Data no calendário gregoriano 
- Ano
- Mês
Coluna 3: Data em fração de ano.
Coluna 4: Total suavizado* mensal de manchas solares. Um valor de -1 indica que não há dados para aquele dia (missing value).
Coluna 5: Desvio padrão mensal da entrada da quantidade de manchas solares inseridas pelas estações individuais.
Coluna 6: Número de observações usadas para computar o total diário (coluna 5).
Coluna 7: Indicador de valor definitivo ou provisório. '1' indica que o valor é definitivo. '0' indica que o valor ainda é provisório.

    * método: tapered-boxcar

---Em TSN_anual, as colunas simbolizam:
Coluna 1: Ano (yyyy.5 - pois a medição foi feita na metade do ano).
Coluna 2: Total anual de manchas solares. Um valor de -1 indica que não há dados para aquele dia (missing value).
Coluna 3: Desvio padrão anual da entrada da quantidade de manchas solares inseridas pelas estações individuais.
Coluna 4: Número de observações usadas para computar o total diário (coluna 5).
Coluna 5: Indicador de valor definitivo ou provisório. '1' indica que o valor é definitivo. '0' indica que o valor ainda é provisório.

Sabendo o que cada coluna coluna indica, podemos montar melhor nossos dicionários de análises.
"""

# print(TSN_diario[1:2]) a indexação funciona por linha
# <dados_diarios> é uma lista com sub-listas de tuplas de mesmo ano.

TSN_dados_diarios = list()
dados_m_ano = list()
for linha in range(len(TSN_diario)):  # Isso pega as linhas

    tupla_dados = tuple()
    if linha == 0:
        ano = TSN_diario.iat[0, 0]

    else:
        ano = TSN_diario.iat[linha - 1, 0]

    for coluna in range(len(TSN_diario.columns)):

        tupla_dados += (TSN_diario.iat[linha, coluna], )

    if tupla_dados[0] == ano and linha < len(TSN_diario) - 1:
        dados_m_ano += [tupla_dados]

    if tupla_dados[0] != ano or linha == len(TSN_diario) - 1:
        TSN_dados_diarios += [dados_m_ano]
        dados_m_ano = []
        dados_m_ano += [tupla_dados]

    del tupla_dados

    ''' 
    Isso gera uma grande lista de tuplas, onde, por mais que os anos estejam em ordem crescente, eles ainda estão
    todos dentro de uma mesma lista. Será interessante criar sub_listas para tuplas de mesmo ano.
    
    Ok, foi corrigido, mas 2023 não está aparecendo.
    
    Agora o 2023 aparece, mas o primeiro dia do ano não.
    Isso acontece porque quando ele encontra, por exemplo, 2022/01/01 ele está comparando com 2021/12/31, então ele 
    não adiciona na tupla. (Corrigido)
    
    Nota, os índices i por ano maiores que ou iguais a 1818 são i = ano_desejado - 1818
    '''

# <dados_mensais_normal> é uma lista com sub-listas de tuplas de mesmo ano
'''TSN_dados_mensais_normal = list()
dados_m_ano = list()
for linha in range(len(TSN_mensal_normal)):  # Isso pega as linhas

    tupla_dados = tuple()
    if linha == 0:
        ano = TSN_mensal_normal.iat[0, 0]
    else:
        ano = TSN_mensal_normal.iat[linha - 1, 0]

    for coluna in range(len(TSN_mensal_normal.columns)):

        tupla_dados += (TSN_mensal_normal.iat[linha, coluna], )

    if tupla_dados[0] == ano and linha < len(TSN_mensal_normal) - 1:
        dados_m_ano += [tupla_dados]

    if tupla_dados[0] != ano or linha == len(TSN_mensal_normal) - 1:
        TSN_dados_mensais_normal += [dados_m_ano]
        dados_m_ano = []
        dados_m_ano += [tupla_dados]

    del tupla_dados

# <dados_mensais_normal> é uma lista com sub-listas de tuplas de mesmo ano
TSN_dados_mensais_suavizado = list()
dados_m_ano = list()
for linha in range(len(TSN_mensal_suavizado)):  # Isso pega as linhas

    tupla_dados = tuple()
    if linha == 0:
        ano = TSN_mensal_suavizado.iat[0, 0]
    else:
        ano = TSN_mensal_suavizado.iat[linha - 1, 0]

    for coluna in range(len(TSN_mensal_suavizado.columns)):

        tupla_dados += (TSN_mensal_suavizado.iat[linha, coluna], )

    if tupla_dados[0] == ano and linha < len(TSN_mensal_suavizado) - 1:
        dados_m_ano += [tupla_dados]

    if tupla_dados[0] != ano or linha == len(TSN_mensal_suavizado) - 1:
        TSN_dados_mensais_suavizado += [dados_m_ano]
        dados_m_ano = []
        dados_m_ano += [tupla_dados]

    del tupla_dados
'''


'''
Para coletar os dados da tabela anual é mais simples, será apenas uma lista de tuplas.
'''

'''
TSN_dados_anuais = list()
for linha in range(len(TSN_anual)):  # Isso pega as linhas

    tupla_dados = tuple()
    for coluna in range(len(TSN_anual.columns)):

        tupla_dados += (TSN_anual.iat[linha, coluna], )

    TSN_dados_anuais += [tupla_dados]

    del tupla_dados
'''