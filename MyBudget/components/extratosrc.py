import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app

# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([
        html.Legend('Tabela de Receitas'),
        html.Div(id='tabela-receitas', className='dbc')
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph2', style={'margin-right': '20px'})
        ], width=9),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Receitas"),
                    html.Legend("R$ 10000", id="valor_receita_card", style={'font-size': '60px'}),
                    html.H6("Total de Receitas")
                ], style={'text-align': 'center', 'padding-top': '30px'})
            ])
        ], width=3)
    ])
], style={'padding': '10px'})

# =========  Callbacks  =========== #
# Tabela
@app.callback(
    Output('tabela-receitas', 'children'),
    Input('store-receitas', 'data')
)
def imprimir_tabela(data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date
    df = df.fillna('-')
    df.sort_values(by='Data', ascending=False)
    
    tabela = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    
    return tabela

@app.callback(
    Output('bar-graph2', 'figure'),
    [Input('store-receitas', 'data'),]
)
def bar_chart(data):
    df = pd.DataFrame(data)
    df_grouped = df.groupby("Categoria").sum()[["valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria', y='valor', title="Receitas Gerais")
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    
    return graph

@app.callback(
    Output('valor_receita_card', 'children'),
    [Input('store-receitas', 'data'),]
)
def display_desp(data):
    df = pd.DataFrame(data)
    valor = df['valor'].sum()
    
    return f"R$ {valor}"