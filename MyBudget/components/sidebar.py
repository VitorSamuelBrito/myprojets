import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd
from globals import*


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("My Buget", className="text-primary"),
    html.P("By Vitor Brito", className="text-info"),
    html.Hr(), 
# -------- Seção Perfil ------
    dbc.Button(id='botao-avatar',
              children=[html.Img(src='/assets/Vitor.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                       ], style={'background-color': 'transparent', 'border-color': 'transparent'}),
# -------- Seção Receita ------
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='open-novo-receita', children=['+ Receita'])
        ],width=6),
        dbc.Col([
            dbc.Button(color='danger', id='open-novo-despesa', children=['- Despesa'])
        ], width=6)
    ]),
# ------ Seção Modal Receita ------
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
        dbc.ModalBody([dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herença...", id="txt-receita"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="$100.00", id="valor_receita", value=""),
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-receitas', 
                                         min_date_allowed=date(2022, 1, 1),
                                         max_date_allowed=date(2050, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                    
                    ),
                ], width=4),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[{'label': 'Foi Recebido', 'value': 1}, {'label': 'Receita Recorrente', 'value': 2}],
                        value=[],
                        id='switches-input-receita',
                        switch=True
                    )
                ], width=4),
                dbc.Col([
                    html.Label('Categoria da receita'),
                    dbc.Select(id='select_receita', 
                               options=[{'label': i, 'value': i} for i in cat_receitas], 
                               value=cat_receitas[0])
                ], width=4)
            ], style={'margin-top': '25px'}),
             dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                html.Hr(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                html.Hr(),
                                html.Div(id="category-div-add-receita", style={}),
                            ], width=6),
                            dbc.Col([
                                html.Legend('Excluir categoria', style={'color': 'red'}),
                                dbc.Checklist(
                                  id='checklist-selected-style-receita',
                                    options=[{'label': i, 'value': i} for i in cat_receitas], 
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'bordercolor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-receita'),
                html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                    dbc.Popover(dbc.PopoverBody("Receita salva"), target="salvar_receita", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
            
        ])
    ], style={"background-color": "rgba(17, 140, 79, 0.05)"}, 
        id='modal-novo-receita', 
        size="lg",
        is_open=False, 
        centered=True, 
        backdrop=True),
# ------ Seção Modal Despesa ------ 
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
        dbc.ModalBody([dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: Gasolina, Casa...", id="txt-despesa"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="$100.00", id="valor_despesa", value=""),
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-despesa', 
                                         min_date_allowed=date(2022, 1, 1),
                                         max_date_allowed=date(2050, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                    
                    ),
                ], width=4),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[{'label': 'Foi pago', 'value': 1}, {'label': 'Despesa Recorrente', 'value': 2}],
                        value=[],
                        id='switches-input-despesa',
                        switch=True
                    )
                ], width=4),
                dbc.Col([
                    html.Label('Categoria da despesa'),
                    dbc.Select(id='select_despesa', 
                               options=[{'label': i, 'value': i} for i in cat_despesas], 
                               value=cat_despesas[0])
                ], width=4)
            ], style={'margin-top': '25px'}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa", value=""),
                                html.Hr(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                html.Hr(),
                                html.Div(id="category-div-add-despesa", style={}),
                            ], width=6),
                            dbc.Col([
                                html.Legend('Excluir categoria', style={'color': 'red'}),
                                dbc.Checklist(
                                  id='checklist-selected-style-despesa',
                                    options=[{'label': i, 'value': i} for i in cat_despesas], 
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'bordercolor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-despesa'),
                html.Div(id='id_teste_despesa', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Despesa", id="salvar_despesa", color="danger"),
                    dbc.Popover(dbc.PopoverBody("Despesa salva"), target="salvar_despesa", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
            
        ])
    ], style={"background-color": "rgba(17, 140, 79, 0.05)"}, 
        id='modal-novo-despesa', 
        size="lg",
        is_open=False, 
        centered=True, 
        backdrop=True),
# ------ Seção de navegação, dashboard e extratos ------
    html.Hr(),
    
    dbc.Nav([
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos Despesas", href="/extratosds", active="exact"),
        dbc.NavLink("Extratos Receitas", href="/extratosrc", active="exact"),
    ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"})
    
    
], id='sidebar_completa')


# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita','is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa','is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
# pop-up salvamento das informações
@app.callback(
    Output('store-receitas', 'data'),
    Input('salvar_receita', 'n_clicks'),
    [
        State('txt-receita', 'value'),
        State("valor_receita", "value"),
        State("date-receitas", "date"),
        State("switches-input-receita", "value"),
        State("select_receita", "value"),
        State('store-receitas', 'data')
    ]
)

def salve_form_receita(n, descricao, valor, date, switches, categoria, dict_receitas):
    
    df_receitas= pd.DataFrame(dict_receitas)
    
    if n and not(valor == "" or valor == None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria
        recebido = 1 if 1 in switches else 0
        fixo = 1 if 2 in switches else 0
        
        df_receitas.loc[df_receitas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_receitas.to_csv("df_receitas.csv")
    
    data_return = df_receitas.to_dict()    
    return data_return

# pop-up salvamento das informações de Despesas
@app.callback(
    Output('store-despesas', 'data'),
    Input('salvar_despesa', 'n_clicks'),
    [
        State('txt-despesa', 'value'),
        State("valor_despesa", "value"),
        State("date-despesa", "date"),
        State("switches-input-despesa", "value"),
        State("select_despesa", "value"),
        State('store-despesas', 'data')
    ]
)

def salve_form_despesa(n, descricao, valor, date, switches, categoria, dict_despesas):
    
    df_despesas= pd.DataFrame(dict_despesas)
    
    if n and not(valor == "" or valor == None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria
        recebido = 1 if 1 in switches else 0
        fixo = 1 if 2 in switches else 0
        
        df_despesas.loc[df_despesas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_despesas.to_csv("df_despesas.csv")
    
    data_return = df_despesas.to_dict()    
    return data_return

# Pop-up excluir e adcionar categorias de despesas
@app.callback(
    [
        Output("select_despesa", "options"),
        Output('checklist-selected-style-despesa', 'options'),
        Output('checklist-selected-style-despesa', 'value'),
        Output('stored-cat-despesas', 'data')],
    
        [Input("add-category-despesa", "n_clicks"),
        Input("remove-category-despesa", 'n_clicks')],
        
        [State("input-add-despesa", "value"),
        State('checklist-selected-style-despesa', 'value'),
        State('stored-cat-despesas', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_despesas= list(data["Categorias"].values())
    
    if n and not (txt == "" or txt == None):
        cat_despesas = cat_despesas + [txt] if txt not in cat_despesas else cat_despesas
        
    if n2:
        if len(check_delete) > 0:
            cat_despesas= [i for i in cat_despesas if i not in check_delete]
            
    opt_despesas = [{"label": i, "value": i} for i in cat_despesas]
    df_cat_despesas = pd.DataFrame(cat_despesas, columns=['Categorias'])
    df_cat_despesas.to_csv("df_cat_despesas.csv")
    data_return = df_cat_despesas.to_dict()
            
    return [opt_despesas, opt_despesas, [], data_return]

# Pop-up excluir e adcionar categorias de receitas
@app.callback(
    [
        Output("select_receita", "options"),
        Output('checklist-selected-style-receita', 'options'),
        Output('checklist-selected-style-receita', 'value'),
        Output('stored-cat-receitas', 'data')],
    
        [Input("add-category-receita", "n_clicks"),
        Input("remove-category-receita", 'n_clicks')],
        
        [State("input-add-receita", "value"),
        State('checklist-selected-style-receita', 'value'),
        State('stored-cat-receitas', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_receitas= list(data["Categorias"].values())
    
    if n and not (txt == "" or txt == None):
        cat_receitas = cat_receitas + [txt] if txt not in cat_receitas else cat_receitas
        
    if n2:
        if len(check_delete) > 0:
            cat_receitas= [i for i in cat_receitas if i not in check_delete]
            
    opt_receitas = [{"label": i, "value": i} for i in cat_receitas]
    df_cat_receitas = pd.DataFrame(cat_receitas, columns=['Categorias'])
    df_cat_receitas.to_csv("df_cat_receitas.csv")
    data_return = df_cat_receitas.to_dict()
            
    return [opt_receitas, opt_receitas, [], data_return]