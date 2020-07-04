# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:20:09 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc
from largegraph import transactions_graph_large, procurement_large
import pandas as pd
from dash_table import DataTable
def subtab1():
    seed = '600971, 611692, 540660, 609913, 470085, 484189, 612711, 602794, 554368'
    return html.Div([
                html.H5('Enter Person Node ID(s)', style={'width': '15%','display':'inline-block'}),
                dcc.Input(id='inp_seed', type='text', value = seed,
                          style={'width': '70%','display':'inline-block'}),
                          
                html.Button('Get Related ID`s', id='fetchNodes', 
                            style={'backgroundColor': 'rgba(200, 200, 210, 0.8)',
                                   'width': '15%','display':'inline-block', 'text-align':'center'}),
                html.Div([]),            
                html.H6(children='Related nodes', style={'width': '10%','display':'inline-block'}),
                dcc.Input(id='out_seed', type='text', value = seed, style={'display':'inline-block','width': '75%'}),
                html.Button('Fetch Transactions', id='fetchTransactions', 
                            style={'backgroundColor': 'rgba(200, 200, 210, 0.8)',
                                   'width': '15%','display':'inline-block', 'text-align':'center'}),
                html.Div([]),            
                html.H6(children='Nodes Order', style={'width': '10%','display':'inline-block'}),
                dcc.Input(id='nodes_order', type='text', style={'display':'inline-block','width': '75%'}),
                html.Button('Reorder Nodes', id='reorder_nodes', 
                            style={'backgroundColor': 'rgba(200, 200, 210, 0.8)',
                                   'width': '15%','display':'inline-block', 'text-align':'center'}),
                dcc.Graph(id='large_transactions', figure = transactions_graph_large(seed))
            ])

def subtab2():
    df = pd.read_csv('data/large/coauthors.csv')
    persons = df['Source'].tolist()
    persons = sorted(list(set(persons)))
    documents = df['Target'].tolist()
    documents = sorted(list(set(documents)))
    dropdown_dict = {'Person': persons, 'Document':documents}
    names = list(dropdown_dict.keys())
    return html.Div([
                html.Div([
                    html.Div([
                            html.H5('Node Type ')
                            ], style={'width':'10%','display':'inline-block', 'text-align':'center'}),
                    html.Div([
                            dcc.Dropdown(id='nodetype',
                                options=[{'label': name, 'value': name} for name in names],
                                value=list(dropdown_dict.keys())[0])
                            ],style={'height': '25px','width': '12%','display':'inline-block'}),
                    html.Div([
                            html.H5('Node')
                            ], style={'width':'6%','display':'inline-block', 'text-align':'center'}),
                    html.Div([
                            dcc.Dropdown(id='node')
                            ],style={'height': '25px','width': '12%','display':'inline-block'}),
                    
                ],style={'width': '100%','display':'inline-block','backgroundColor': 'rgba(105, 105, 105, 0.9)'}),
                html.Div([
                        DataTable(id='coauthors_table',data=[],
                          style_header={'backgroundColor': 'rgb(30, 30, 30)', 'fontWeight': 'bold',
                                        'fontSize':20},
                          style_cell={'backgroundColor': 'rgb(50, 50, 50)',
                                      'color': 'white', 'fontSize':20},)
                        ],style={'width':'80%', 'text-align':'center','padding-left':'10%'}) 
            ])
            
def subtab3():
    df = pd.read_csv('data/large/sales.csv')
    items = df['Target']
    items = sorted(list(set(items)))
    return html.Div([
                html.Div([
                    html.Div([
                            html.H5('Select Item ')
                            ], style={'width':'10%','display':'inline-block', 'text-align':'center'}),
                    html.Div([
                            dcc.Dropdown(id='item_node',
                                options=[{'label': name, 'value': name} for name in items],
                                value=items[0])
                            ],style={'height': '25px','width': '12%','display':'inline-block'}),
                ],style={'width': '100%','display':'inline-block','backgroundColor': 'rgba(105, 105, 105, 0.9)'}),
                html.Div([
                        dcc.Graph(id='procurement', figure = procurement_large(items[0]))
                        ]) 
            ])
    
if __name__ == "__main__":
    subtab1()