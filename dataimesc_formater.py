import pandas as pd
#Entrada de dados no sistema

colunas=input("Insira as colunas fixas do excel: ")

anos=input("Insira os anos divididos por vírgula: ")
anos=anos.split("\t")
print(anos)
anos=[i.strip() for i in anos]
print(anos)
anos=[int(ano) for ano in anos]

#Tratamento dos dados inputados
entrada="C:\\Users\\Mario.Sousa\\Downloads\\serieacimadecinco.xlsx"
columns=colunas.split("\t")
columns=[i.strip() for i in columns]
print(columns)
dataframe=pd.read_excel(entrada)
print(dataframe)
dataframe2=pd.melt(dataframe,id_vars=columns,value_vars=anos)
dataframe2.to_excel("serie727.xlsx",index=False)
print("Finalizado")
