from pysus.online_data.sinasc import download
df = download('SE', 2015)
df.head()

'''
import json
import requests

from pandas.json_normalize import json_normalize


#API de comunicação com datasus
def datasus_communication_request():
    try:
        url = "https://imunizacao-es.saude.gov.br/_search"
        payload = "{\r\n    \"size\": 10\r\n}"
        headers = {
            'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        transform_dataset_analyze(response.text)
    except Exception as e:
        print(e)

#função de criação de dataset
def transform_dataset_analyze(response):
    resul = json.loads(response)
    df = json_normalize(resul["hits"]["hits"])
    print(df)


#método main para chamar os demais métodos
if __name__ == '__main__':
    datasus_communication_request()
'''
