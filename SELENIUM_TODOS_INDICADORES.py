import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

df = {'indice':[],'titulo':[]}

for i in range(1,2000):
    url = 'http://dataimesc.imesc.ma.gov.br/series/'+str(i)+'/show'
    reqs = rq.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('h2',{'class':'p-2 title'}):
        df['indice'].append(i)
        df['titulo'].append(title.get_text())

data = pd.DataFrame(df)
data.to_excel('teste_site.xlsx',index=False)
