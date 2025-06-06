from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import sidebar
from components import extratosds
from components import dashboards
from components import extratosrc

from app import *
from globals import*



# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dcc.Store(id='store-receitas', data=df_receitas.to_dict()),
    dcc.Store(id='store-despesas', data=df_despesas.to_dict()),
    dcc.Store(id='stored-cat-receitas', data=df_cat_receitas.to_dict()),
    dcc.Store(id='stored-cat-despesas', data=df_cat_despesas.to_dict()),
    
    dbc.Row([dbc.Col([ dcc.Location(id='url'),
            sidebar.layout 
        ], md=2), dbc.Col([
            content ], md=10) 
            ])

], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')]) 
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extratosds':
        return extratosds.layout
    
    if pathname == '/extratosrc':
        return extratosrc.layout
    


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)