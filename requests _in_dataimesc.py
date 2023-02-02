import requests as rq
import pandas as pd
x=range(2098,3000)
pandao=pd.DataFrame()
for f in x:
    requi=rq.get(f"http://dataimesc.imesc.ma.gov.br/getData?id={f}&scope=4&from=2010&to=2021")
    requi=requi.json()
    requi_series=requi["values"]
    lista_a=[]
    lista_b=[]
    for i,h in requi_series.items():
        lista_a.append(i)
        lista_b.append(h)
    lista_a=pd.DataFrame(lista_a)
    lista_b=pd.DataFrame(lista_b)
    lista_c=pd.concat([lista_a,lista_b],axis=1)
    lista_k=[]
    lista_m=[]
    lista_cajapio=lista_c[lista_c[0]=="2102408"]
    lista_cajapio["variavel"]=f
    pandao=pd.concat([pandao,lista_cajapio],axis=0)
    print(pandao)
    print("feito")
    
pandao.to_excel("educacao2.xlsx")
print("Programa Encerrado")
