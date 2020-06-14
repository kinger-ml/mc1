# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:16:11 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc
from transaction_plot import transactions_graph

def dropdown_graphs():
    return html.Div([ 
                dcc.Dropdown(
                    id='graph_name',
                    options=[
                            {'label': 'Template Graph', 'value': 'data/template/'},
                            {'label': 'Subgraph 1', 'value': 'data/G1/'},
                            {'label': 'Subgraph 2', 'value': 'data/G2/'},
                            {'label': 'Subgraph 3', 'value': 'data/G3/'},
                            {'label': 'Subgraph 4', 'value': 'data/G4/'},
                            {'label': 'Subgraph 5', 'value': 'data/G5/'},
                            {'label': 'LARGE GRAPH (Select Seed)', 'value': 'data/large/'},
                            ],
                    value='data/template/'
                    )],style={'height': '25px', 'width': '20%','display':'inline-block'})
    
def dropdown_seeds():
    return html.Div([
                dcc.Dropdown(
                    id='seeds',
                    options=[
                            {'label': 'SEED 0', 'value': '0'}, 
                            {'label': 'SEED 1', 'value': '1'},
                            {'label': 'SEED 2', 'value': '2'}, 
                            {'label': 'SEED 3', 'value': '3'},
                            {'label': 'SEED 4', 'value': '4'}, 
                            {'label': 'SEED 5', 'value': '5'}
                            ],
                    value='0'
                )
                ], style={'height': '25px', 'width': '15%','display':'inline-block'})
                
def div_transactions():
    return html.Div([
                html.Div([
                    html.H4('TRANSACTIONS')
                    ],style={'width': '16%','display':'inline-block', 
                            'backgroundColor': 'rgba(105, 105, 105, 0.2)',
                            'text-align':'center', 'color': 'maroon',
                            'font-weight': 'bold'}),
                html.Div([
                    html.H5('Select Subgraph')
                    ],style={'width': '13%','display':'inline-block',
                            'text-align':'center'}),
            dropdown_graphs(),
            dropdown_seeds()
            ], style={'backgroundColor': 'rgba(0, 0, 240, 0.3)'})
                
def div_statistics():
    return html.Div([
                html.Div([
                    html.H4('STATISTICS')
                    ],style={'width': '16%','display':'inline-block', 
                            'backgroundColor': 'rgba(105, 105, 105, 0.2)',
                            'text-align':'center', 'color': 'maroon',
                            'font-weight': 'bold'})
            ], style={'backgroundColor': 'rgba(100, 100, 240, 0.3)'})