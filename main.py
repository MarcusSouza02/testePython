import pandas as pd

data_1 = pd.read_excel("data/Carros.xlsx")
data_2 = pd.read_excel("data/Marcas.xlsx")

data_filter = data_1[data_1["Ano"] >=2018]

data_teste = data_1[data_1["Marca"].isin(data_2["Marca"])]

print(data_teste)


