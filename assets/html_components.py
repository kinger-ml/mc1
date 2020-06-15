# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:16:11 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc

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
                
def dropdown_graphs2():
    return html.Div([ 
                dcc.Dropdown(
                    id='graph_name2',
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
                    )],style={'height': '25px', 'width': '18%','display':'inline-block'})

def dropdown_channel():
    return html.Div([ 
                dcc.Dropdown(
                    id='channel',
                    options=[
                            {'label': 'CALLS', 'value': 'calls'},
                            {'label': 'EMAILS', 'value': 'emails'},
                            {'label': 'TRAVEL', 'value': 'travel'},
                            ],
                    value='calls'
                    )],style={'height': '25px', 'width': '10%','display':'inline-block'})
    
def dropdown_charts():
    return html.Div([ 
                dcc.Dropdown(
                    id='charts',
                    options=[
                            {'label': 'Heatmap', 'value': 'heatmap'},
                            {'label': 'Sunburst (By Source)', 'value': 'sunburst1'},
                            {'label': 'Sunburst (By Month)', 'value': 'sunburst2'},
                            ],
                    value='heatmap'
                    )],style={'height': '25px', 'width': '15%','display':'inline-block'})
                
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
            dropdown_graphs()
            ], style={'backgroundColor': 'rgba(0, 0, 240, 0.3)'})
                
def div_statistics():
    return html.Div([
                html.Div([
                    html.H4('STATISTICS')
                    ],style={'width': '16%','display':'inline-block', 
                            'backgroundColor': 'rgba(105, 105, 105, 0.2)',
                            'text-align':'center', 'color': 'maroon',
                            'font-weight': 'bold'}),
                html.Div([
                    html.H5('Select Subgraph')
                    ],style={'width': '13%','display':'inline-block',
                            'text-align':'center'}),
                dropdown_graphs2(),
                
                html.Div([
                    html.H5('Channel')
                    ],style={'width': '8%','display':'inline-block',
                            'text-align':'center'}),
                dropdown_channel(),
                
                html.Div([
                    html.H5('Chart')
                    ],style={'width': '7%','display':'inline-block',
                            'text-align':'center'}),
                dropdown_charts(),
            ], style={'backgroundColor': 'rgba(0, 0, 240, 0.3)'})
                
def div_coauthors():
    return html.Div([
                html.Div([
                    html.H4('CO-AUTHORS')
                    ],style={'width': '16%','display':'inline-block', 
                            'backgroundColor': 'rgba(105, 105, 105, 0.2)',
                            'text-align':'center', 'color': 'maroon',
                            'font-weight': 'bold'})
            ], style={'backgroundColor': 'rgba(10, 100, 140, 0.3)'})

def div_demographics():
    return html.Div([
                html.Div([
                    html.H4('DEMOGRAPHICS')
                    ],style={'width': '16%','display':'inline-block', 
                            'backgroundColor': 'rgba(105, 105, 105, 0.2)',
                            'text-align':'center', 'color': 'maroon',
                            'font-weight': 'bold'})
            ], style={'backgroundColor': 'rgba(10, 200, 40, 0.3)'})   