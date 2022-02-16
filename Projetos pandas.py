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
print("A base de dados apresenta {} regitros (imoveis) e {} variáveis.".format(dados.shape[0], dados.shape[1]))