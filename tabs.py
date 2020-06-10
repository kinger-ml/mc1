# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:59:10 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc
from transaction_plot import transactions_graph
def tab1():
    return html.Div([
                html.Div([ 
                    dcc.Dropdown(
                        id='graph_name',
                        options=[
                                {'label': 'Template Graph', 'value': 'data/template/'},
                                {'label': 'Subgraph 1', 'value': 'data/G1/'},
                                {'label': 'Subgraph 2', 'value': 'data/G2/'},
                                {'label': 'Subgraph 3', 'value': 'data/G3/'},
                                {'label': 'Subgraph 4', 'value': 'data/G4/'},
                                {'label': 'Subgraph 5', 'value': 'data/G5/'},
                                {'label': 'LARGE GRAPH', 'value': 'data/all/'},
                                ],
                        value='data/template/'
                        )],style={'width': '50%','display':'inline-block'}),
    
                html.Div([
                        dcc.Dropdown(
                            id='person',
                            options=[
                                    {'label': '0', 'value': '0'}, {'label': '1', 'value': '1'},
                                    {'label': '2', 'value': '2'}, {'label': '3', 'value': '3'},
                                    {'label': '4', 'value': '4'}, {'label': '5', 'value': '5'},
                                    {'label': '6', 'value': '6'}, {'label': '7', 'value': '7'},
                                    {'label': '8', 'value': '8'}, {'label': '9', 'value': '9'}
                                    ],
                            value='0'
                        )
                    ], style={'width': '50%','display':'inline-block', 'float': 'right'}),
                 html.Div([
                         dcc.Graph(id='transaction', figure=transactions_graph('data/template/'))
                         ])
                
        ])

def tab2():
    return html.Div([
            html.H3('Launching Soon!!!!')
        ])

def tab3():
    fig1 = transactions_graph('data/template/')
    fig1.update_xaxes(rangeslider_visible=False)
    fig1.update_layout(
            legend_orientation="v",
            height=400,
            margin=dict(
                        l=50,
                        r=50,
                        b=1,
                        t=10,
                        pad=4
                        )
            
    )
    fig2 = transactions_graph('data/G1/')
    fig2.update_xaxes(rangeslider_visible=False)
    fig2.update_layout(
            legend_orientation="v",
            height=400,
            margin=dict(
                        l=50,
                        r=50,
                        b=10,
                        t=10,
                        pad=4
                        )
    )
    return html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2),
        ])

if __name__ == "__main__":
    tab1()
