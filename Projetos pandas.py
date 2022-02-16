# Relatório de análise 1

import pandas as pd

dados = pd.read_csv("aluguel.csv/aluguel.csv", sep=';')
type(dados)

dados.info()
dados.head()

# Informações gerais sobre a base de dados

dados.dtypes
tipos_de_dados = pd.DataFrame(dados.dtypes, columns= ["Tipos de dados"])
tipos_de_dados.columns.name = "Variáveis"
tipos_de_dados

dados.shape
print("A base de dados apresenta {} regitros (imóveis) e {} variáveis.".format(dados.shape[0], dados.shape[1]))

tipos_de_imovel = dados["Tipo"]

type(tipos_de_imovel)

# Removendo duplicadas
tipos_de_imovel.drop_duplicates(inplace = True)

tipos_de_imovel = pd.DataFrame(tipos_de_imovel)
tipos_de_imovel.index = range(tipos_de_imovel.shape[0])

