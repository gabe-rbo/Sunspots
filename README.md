# Trabalho Prático A de Programação de Computadores - **MANCHAS SOLARES**.
## Por Gabriel Ribeiro (TM1) - UFMG, 2023.

#%% md
### Uma breve introdução às manchas:

Manchas solares, ou _Sunspots_ - como são chamadas em inglês, são regiões mais escuras da superfície solar. Elas ocorrem, pois o sol possui moléculas gasosas super-carregadas eletricamente, cujo movimento constante resulta em perturbações extremas no campo eletromagnético da estrela. Essas perturbações, quando muito fortes, fazem com que o campo prenda o calor solar, criando Manchas Solares na superfície, regiões menos quentes que sua vizinhança. 
Mais cientificamente, explica a NASA:

> Sunspots:  One interesting aspect of the Sun is its sunspots.  Sunspots are areas where the magnetic field is about 2,500 times stronger than Earth's, much higher than anywhere else on the Sun.  Because of the strong magnetic field, the magnetic pressure increases while the surrounding atmospheric pressure decreases.  This in turn lowers the temperature relative to its surroundings because the concentrated magnetic field inhibits the flow of hot, new gas from the Sun's interior to the surface. 

> Manchas solares: Um aspecto interessante do Sol são suas manchas. Manchas solares são áreas onde o campo magnético é quase 2,500 vezes mais forte que o da Terra, mais forte ainda que em qualquer outro lugar do Sol. Devido ao forte campo magnético, a pressão magnética aumenta enquanto a pressão atmosférica ao redor diminui. Isso diminui a temperatura relativa à sua vizinhança porque a concentração do campo magnético impede o fluxo de novo gás quente do interior do Sol à superfície.

O número de manchas solares é importante, pois define o quão profundo no ciclo solar estamos. A queda, ascensão e nova queda no número de manchas implica entrada e saída de um novo ciclo. Desde que começaram a ser estudados, em 1749, no Observatório de Zurique na Suíça, a humanidade já atravessou 23 ciclos solares, estando agora no 24.º. Além disso, há teorias e evidências científicas que implicam, fortemente, relações entre a atividade solar e o clima do planeta Terra. Por exemplo, entre 1645 e 1715, período conhecido como Pequena Era do Gelo para algumas partes do globo, é conhecido, no campo de pesquisas solares, de Mínimo de Maunder (_Maunder Minimum_). Outrora, em períodos de máximos solares, há um pequeno aumento na energia liberada pelo sol. Mesmo que isso não afete fortemente o planeta, o número de raios ultravioleta emitidos cresce bastante, resultando em uma alteração na mecânica da atmosfera terrestre. Não somente, nos períodos de máximas, o número de ejeções de massa solar cresce, devido à forte presença do campo eletromagnético na superfície, esses _Solar Flares_ resultam em um lançamento massivo de raios-x e campos eletromagnéticos, causando uma tempestade geomagnética no planeta Terra, gerando um aumento em Auroras Boreais, perturbações de rádio e na matriz elétrica humana. 

###### Fontes: https://www.weather.gov/fsd/sunspots#:~:text=Sunspots%20are%20areas%20where%20the,the%20surrounding%20atmospheric%20pressure%20decreases ; https://spaceplace.nasa.gov/solar-activity/en/

### Objetivos:

Este trabalho tem como objetivo fazer uma amadora análise do número de manchas solares no decorrer do tempo, usando da linguagem Python e com algumas bibliotecas, como Datetime e Matplotlib, para auxiliar nas células de dados.

### Execuções:

A única base de dados utilizada nesta análise são os dados diários de manchas solares da SilSo (https://www.sidc.be/SILSO/datafiles). Essa escolha foi feita devido à ausência de consistência nos dados. Mesmo ambas as tabelas apresentando valores definitivos, quando analizadas lado a lado, algumas inconsistências - como, por exemplo, diferença em quantidades de manchas solares por ano - foram encontradas. Tanto é que, em primeiro plano, a ideia de meu trabalho era expor isso e conseguir assumir e deduzir ainda mais informações sobre os dados coletados pela SilSo. No entanto, isto se provou bastante complicado, pois há uma base de dados grande para ser analisada e também devido aos tratamentos de entrada para cada base de dados para contato com usuário. 
Originalmente, este trabalho possuía 3 pivôs de dados, com todas as suas sub-informações disponíveis no site da SilSo: TSN - Total Sunspot Number -, HSN - Hemispheric Sunspot Number -, DESN - Daily Estimated Sunspot Number. Devido à falta de tempo, para não entregar meio-trabalho, reduzi à TSN - Diário, para, também, fugir de inconsistências conclusíveis.

Além disso, tomei para mim outra modificação: o tratamento dos dados não é realizado por meio de dicionários. Optei por utilizar matrizes. Isto, pois a presença da base de dados bem documentada auxilia. Além disso, a matriz (_array_) permitiria trabalhar com um número maior de ferramentas, como àquelas disponíveis por Pandas, caso fosse preciso.
O tratamento da tabela em .csv (_comma separated value_) é feita na pasta Total_sunspot_number, com o módulo base_de_dados_TSN. Este cria algumas variáveis globais de análise que seriam utilizadas para compor toda a análise da parte TSN, mas está sendo utilizada apenas <dados_diarios_TSN>, como já foi previamente justificado.

O trabalho, agora, possui uma célula para auxiliar no tratamento de entrada e outras 8 funções para manipulação de dados. Todas as quais serão devidamente explicadas. No final, há uma função de interface, que culmina tudo que há no programa.
