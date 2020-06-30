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
                            {'label': 'Sunburst (By Target)', 'value': 'sunburst3'},
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
                
def tab3_left():
    return html.Div([
                html.H6('Select Subgraph'),
                dcc.Dropdown(
                    id='graph_name_match',
                    options=[
                            {'label': 'Subgraph 1', 'value': 'data/G1/'},
                            {'label': 'Subgraph 2', 'value': 'data/G2/'},
                            {'label': 'Subgraph 3', 'value': 'data/G3/'},
                            {'label': 'Subgraph 4', 'value': 'data/G4/'},
                            {'label': 'Subgraph 5', 'value': 'data/G5/'},
                            {'label': 'LARGE GRAPH (Select Seed)', 'value': 'data/large/'},
                            ],
                    value='data/G1/'
                    ),
                html.H6('Select Chart'),
                dcc.Dropdown(
                    id='chart_name_match',
                    options=[
                            {'label': 'Transactions', 'value': 'transactions'},
                            {'label': 'Coauthorship', 'value': 'coauthorship'},
                            {'label': 'Spending Demographics', 'value': 'demographicsS'},
                            {'label': 'Earning Demographics', 'value': 'demographicsR'},
                            {'label': 'Call Stats - Heatmap', 'value': 'callstat_heatmap'},
                            {'label': 'Call Stats - Sunburst(Source)', 'value': 'callstat_sunburst1'},
                            {'label': 'Call Stats - Sunburst(Month)', 'value': 'callstat_sunburst2'},
                            {'label': 'Call Stats - Sunburst(Target)', 'value': 'callstat_sunburst3'},
                            
                            {'label': 'Email Stats - Heatmap', 'value': 'emailstat_heatmap'},
                            {'label': 'Email Stats - Sunburst(Source)', 'value': 'emailstat_sunburst1'},
                            {'label': 'Email Stats - Sunburst(Month)', 'value': 'emailstat_sunburst2'},
                            {'label': 'Email Stats - Sunburst(Target)', 'value': 'emailstat_sunburst3'},
                            
                            {'label': 'Travel Stats - Heatmap', 'value': 'travelstat_heatmap'},
                            {'label': 'Travel Stats - Sunburst(Source)', 'value': 'travelstat_sunburst1'},
                            {'label': 'Travel Stats - Sunburst(Month)', 'value': 'travelstat_sunburst2'},
                            {'label': 'Travel Stats - Sunburst(Target)', 'value': 'travelstat_sunburst3'},
                            ],
                    value='transactions'
                    ),
                
                ],style={'width': '96%', 'height': '800px', 'display':'inline-block', 
                    'backgroundColor': 'rgba(105, 105, 105, 0.9)'})    