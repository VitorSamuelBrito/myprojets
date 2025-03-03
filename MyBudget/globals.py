import pandas as pd
import os

if("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
    df_receitas["Data"]= pd.to_datetime(df_receitas["Data"])
    df_despesas["Data"]= pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"]= df_receitas["Data"].apply(lambda x: x.date())
    df_despesas["Data"]= df_despesas["Data"].apply(lambda x: x.date())
    
else:
    data_structure = {'valor': [], 'Efetuado': [], 'Fixo': [], 'Data': [], 'Categoria': [], 'Descrição': []}
    df_receitas = pd.DataFrame(data_structure)
    df_receitas.to_csv("df_receitas.csv")
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    
if("df_cat_despesas.csv" in os.listdir()) and ("df_cat_receitas.csv" in os.listdir()):
    df_cat_despesas = pd.read_csv("df_cat_despesas.csv", index_col=0, parse_dates=True)
    df_cat_receitas = pd.read_csv("df_cat_receitas.csv", index_col=0, parse_dates=True)
    cat_receitas = df_cat_receitas.values.tolist()
    cat_despesas = df_cat_despesas.values.tolist()
    
else:
    cat_receitas = {'Categorias': ["Salário", "Investimento", "Comissão"]}
    cat_despesas = {'Categorias': ["Alimentação", "Gasolina", "Saúde"]}
    
    df_cat_receitas = pd.DataFrame(cat_receitas, columns=['Categorias'])
    df_cat_despesas = pd.DataFrame(cat_despesas, columns=['Categorias'])
    df_cat_receitas.to_csv("df_cat_receitas.csv")
    df_cat_despesas.to_csv("df_cat_despesas.csv")