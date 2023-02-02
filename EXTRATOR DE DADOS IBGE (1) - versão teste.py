import PySimpleGUI as sg
import pandas as pd
import numpy as np

#Repositório de variáveis 
tabelas=[]
planilha=[]
planilhas={}
count=1
pandao=pd.DataFrame()
dicio_estado= {'Tabela1':'Região Norte',
               'Tabela2':'Rondônia',
               'Tabela3':'Acre',
               'Tabela4':'Amazonas',
               'Tabela5':'Roraima',
               'Tabela6': 'Pará',
               'Tabela7':'Amapá',
               'Tabela8':'Tocantins',
               'Tabela9':'Região Nordeste',
               'Tabela10':'Maranhão',
               'Tabela11':'Piauí',
               'Tabela12':'Ceará',
               'Tabela13':'Rio Grande do Norte',
               'Tabela14':'Paraíba',
               'Tabela15':'Pernanbuco',
               'Tabela16':'Alagoas',
               'Tabela17':'Sergipe',
               'Tabela18':'Bahia',
               'Tabela19':'Região Suldeste',
               'Tabela20':'Minas Gerais',
               'Tabela21':'Espírito Santo',
               'Tabela22':'Rio de Janeiro',
               'Tabela23':'São Paulo',
               'Tabela24':'Região Sul',
               'Tabela25':'Paraná',
               'Tabela26':'Santa Catarina',
               'Tabela27':'Rio Grande do Sul',
               'Tabela28':'Região Centro-Oeste',
               'Tabela29':'Mato Grosso do Sul',
               'Tabela30': 'Mato Grosso',
               'Tabela31': 'Goiás',
               'Tabela32':'Distrito Federal',
               'Tabela33': 'Brasil'}
dicio_abrangencia= {'Tabela1':'2',
                    'Tabela2':'3',
                    'Tabela3':'3',
                    'Tabela4':'3',
                    'Tabela5':'3',
                    'Tabela6': '3',
                    'Tabela7':'3',
                    'Tabela8':'3',
                    'Tabela9':'2',
                    'Tabela10':'3',
                    'Tabela11':'3',
                    'Tabela12':'3',
                    'Tabela13':'3',
                    'Tabela14':'3',
                    'Tabela15':'3',
                    'Tabela16':'3',
                    'Tabela17':'3',
                    'Tabela18':'3',
                    'Tabela19':'2',
                    'Tabela20':'3',
                    'Tabela21':'3',
                    'Tabela22':'3',
                    'Tabela23':'3',
                    'Tabela24':'2',
                    'Tabela25':'3',
                    'Tabela26':'3',
                    'Tabela27':'3',
                    'Tabela28':'2',
                    'Tabela29':'3',
                    'Tabela30': '3',
                    'Tabela31': '3',
                    'Tabela32':'3',
                    'Tabela33': '1'}
dicio_codigo= {'Tabela1':'N',
               'Tabela2':'RO',
               'Tabela3':'AC',
               'Tabela4':'AM',
               'Tabela5':'RR',
               'Tabela6': 'PA',
               'Tabela7':'AP',
               'Tabela8':'TO',
               'Tabela9':'NE',
               'Tabela10':'MA',
               'Tabela11':'PI',
               'Tabela12':'CE',
               'Tabela13':'RN',
               'Tabela14':'PB',
               'Tabela15':'PE',
               'Tabela16':'AL',
               'Tabela17':'SE',
               'Tabela18':'BA',
               'Tabela19':'SE',
               'Tabela20':'MG',
               'Tabela21':'ES',
               'Tabela22':'RJ',
               'Tabela23':'SP',
               'Tabela24':'S',
               'Tabela25':'PR',
               'Tabela26':'SC',
               'Tabela27':'RS',
               'Tabela28':'CO',
               'Tabela29':'MS',
               'Tabela30': 'MT',
               'Tabela31': 'GO',
               'Tabela32':'DF',
               'Tabela33': 'BR'}
dicio_planilha={'.1':'Total das Atividades',
                '.2':'Agricultura, inclusive apoio à agricultura e a pós-colheita',
                '.3':'Pecuária, inclusive apoio à Pecuária',
                '.4':'Produção florestal, pesca e aquicultura',
                '.5':'Indústrias extrativas',
                '.6':'Indústrias de transformação',
                '.7':'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação',
                '.8':'Construção','.9':'Comércio e reparação de veículos automotores e motocicletas',
                '10':'Transporte, Armazenagem e correio',
                '11':'Alojamento e alimentação',
                '12':'Informação e comunicação',
                '13':'Atividades financeiras, de seguros e serviços relacionados',
                '14':'Atividades imobiliárias',
                '15':'Atividades profissionais científicas e técnicas, administrativas e serviços complementares',
                '16':'Administração, defesa, educação e saúde públicas e seguridade social',
                '17':'Educação e saúde privadas',
                '18':'Artes, cultura, esporte e recreação e outras atividades de serviços',
                '19':'Serviços domésticos'}

dicio_serie={'.1':'233',
             '.2':'234',
             '.3':'234',
             '.4':'234',
             '.5':'236',
             '.6':'237',
             '.7':'238',
             '.8':'239',
             '.9':'241',
             '10':'242',
             '11':'243',
             '12':'244',
             '13':'245',
             '14':'246',
             '15':'247',
             '16':'248',
             '17':'249',
             '18':'xx',
             '19':'250'}

name_inside={'Total das Atividades':'do Total das Atividades (em mil R$)',
             'Agricultura, inclusive apoio à agricultura e a pós-colheita':'da Agropecuária (em mil R$)',
             'Pecuária, inclusive apoio à Pecuária':'da Agropecuária (em mil R$)',
             'Produção florestal, pesca e aquicultura':'da Agropecuária (em mil R$)',
             'Indústrias extrativas':'da Indústrias extrativas (em mil R$)',
             'Comércio e reparação de veículos automotores e motocicletas':'de Comércio e reparação de veículos automotores e motocicletas (em mil R$)',
             'Artes, cultura, esporte e recreação e outras atividades de serviços':'de Outras atividades de serviços (em mil R$)',
             'Indústrias de transformação':'da Indústrias de Transformação (em mil R$)',
             'Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação':'da Eletricidade e gás, água, esgoto, atividades de gestão de resíduos e descontaminação (em mil R$)',
             'Construção':'da Construção (em mil R$)',
             'Transporte, Armazenagem e correio':'do Transporte, armazenagem e correio (em mil R$)',
             'Informação e comunicação':' da Informação e comunicação',
             'Alojamento e alimentação':'de Alojamento e alimentação (em mil R$)',
             'Informação e comunicação':'de Informação e comunicação (em mil R$)',
             'Atividades financeiras, de seguros e serviços relacionados':'das Atividades financeiras, de seguros e serviços relacionados',
             'Atividades imobiliárias':'das Atividades Imobiliárias (em mil R$)',
             'Atividades profissionais científicas e técnicas, administrativas e serviços complementares':'das Atividades profissionais, científicas e técnicas, administrativas e serviços complementares (em mil R$)',
             'Administração, defesa, educação e saúde públicas e seguridade social':'da Administração, defesa, educação e saúde públicas e seguridade social (em mil R$)',
             'Educação e saúde privadas':'da Educação e saúde privadas (em mil R$)',
             'Serviços domésticos':'de Outras atividades de serviços (em mil R$)',}


def criar_nome():
    #Função que cria o nome das tabelas utilizadas
    for i in range(1,34):
        tabelas.append("Tabela"+str(i))
    for j in tabelas:
        planilha=[]
        planilhas[j]=planilha
        count=1
        for i in range(19):
            planilha.append((j+"."+str(count)))
            count=int(count)
            count+=1
            
def procurar_tabela(plan,tab,loca):
    #Função que busca as tabelas na localização
    print("a tabela é", tab)
    x=pd.read_excel(loca+'\\'+plan+".xls", sheet_name=tab)
    y=pd.DataFrame(x)
    y=y.drop(labels=[0,1,2,3,4,15,16,17,18,19,20,31,32,33,34,35,36,47],axis=0)
    y.insert(0, "Região e UF", dicio_estado[plan] , allow_duplicates=True)
    teste=tab[-2]+tab[-1]
    print("O teste é",teste)
    name=dicio_planilha[teste]
    y["Abrangência"]=dicio_abrangencia[plan]
    y["Código"]=dicio_codigo[plan]
    y.insert(0, "Setor", name , allow_duplicates=True)
    y['Indicador']=y.index
    y['Serie']=dicio_serie[teste]
    y.replace(np.nan,0,inplace=True)
    y['Indicador'].replace([5,6,7,8,9,10,11,12,13,14],f"Valor Bruto da Produção {name_inside[name]}",inplace=True)
    y['Indicador'].replace([21,22,23,24,25,26,27,28,29,30],f"Consumo intermediário {name_inside[name]}",inplace=True)
    y['Indicador'].replace([37,38,39,40,41,42,43,44,45,46],f"Valor Adicionado Bruto {name_inside[name]}",inplace=True)
    y= y.replace(np.nan, 0)
    print(y)
    return y


sg.theme('DarkAmber')   # Define o tema da Janela
# Configuração da Janela
layout = [
            [sg.Text('Para extrair os arquivos, por favor insira')],
            [sg.Text('Local do arquivo:'), sg.InputText('',key='local')],
            [sg.Text('Nome da tabela :'), sg.InputText('',key='nome')],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Criando a Janela
window = sg.Window('EXTRATOR DE ARQUIVOS DO IBGE', layout, size=(600,150))
# Loop de Eventos que irá durar até que a janela seja fechada
while True:
    event, values = window.read()
    local=values['local']
    nome=values['nome']
    perc=0
    if event=='Ok':
        
        #Abrindo a janela de loading
        layout2 =[[sg.Text(f"Pressione 'Executar' e aguarde...")],
            [sg.ProgressBar(33, orientation='h', size=(45,20), border_width=4, key='-PROGRESS_BAR-', bar_color=("Blue", "Yellow"))],
        [sg.Button('Executar'), sg.Exit()]]
        window=sg.Window("Progress Bar", layout2)
        while True:
            pandao=pd.DataFrame()
            event,values=window.read()
            load=0
            if event=="Executar":
                event,values=window.read(1000)     
                criar_nome()
                print(tabelas)
                print(planilhas)
                for sinal in planilhas.keys():
                    load+=1
                    table=planilhas[sinal]
                    perc+=1
                    window['-PROGRESS_BAR-'].update(load)
                    for tabela in table:
                        proc=procurar_tabela(sinal,tabela,local)
                        pandao=pd.concat([pandao,proc])
                        
                #Tratando e transformando as tabelas em excel 
                panda=pandao.rename(columns={'CONTAS REGIONAIS DO BRASIL': 'Ano','Unnamed: 1': 'Valor do ano anterior', 'Unnamed: 2':'Índice de Volume','Unnamed: 3':'Valor a preços do ano anterior', 'Unnamed: 4':'Índice de preço', 'Unnamed: 5':'Valor a preços correntes'}) 
                df_agro=panda.loc[panda["Indicador"]=="Valor Adicionado Bruto da Agropecuária (em mil R$)"]
                s = pd.Series(np.arange(0,len(panda)))
                pandinha=panda.set_index([s]) 
                pandinha.drop(pandinha[pandinha["Indicador"]=="Valor Adicionado Bruto da Agropecuária (em mil R$)"].index, inplace=True)
                df_agro = df_agro.groupby(['Serie','Ano', 'Região e UF','Abrangência', 'Código'],as_index = False).sum(numeric_only=True)
                df_agro["Setor"]="Agricultura e Pecuária"
                df_agro["Indicador"]="Valor Adicionado Bruto da Agropecuária (em mil R$)"
                pandao=pd.concat([pandinha,df_agro])
                s2 = pd.Series(np.arange(0,len(pandao)))
                panda_final=pandao.set_index([s2])
                panda_final=panda_final[["Serie","Setor","Região e UF","Ano","Valor a preços correntes","Abrangência","Código","Indicador"]]
                panda_final.to_excel(local+"\\"+nome+".xlsx")
                x=(local+"\\"+nome+".xlsx")
                sg.Popup("Busca encerrada! Arquivo está disponível no local: ",x)
            if event=="Exit" or event==sg.WIN_CLOSED:
                break
            
    if event== sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    

window.close()
