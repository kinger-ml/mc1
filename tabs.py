# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:59:10 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc
from transaction_plot import transactions_graph
from assets.html_components import div_transactions, div_coauthors, div_demographics
from assets.html_components import div_statistics, tab3_left
from coauthors_plot import coauthors_plot
from stats_plot import statsPlot
from demographics_plot import demographics_spent, demographics_received
from matching_plots import transaction
def tab1():
    return html.Div([
                div_transactions(),
                html.Div([
                     dcc.Graph(id='transaction', figure=transactions_graph('data/template/'))
                     ]),
                div_coauthors(),
                html.Div([
                     dcc.Graph(id='coauthors', figure=coauthors_plot('data/template/'))
                     ]),
                div_demographics(),
                html.Div([
                     dcc.Graph(id='dem_spend', figure=demographics_spent('data/template/'))
                     ]),
                html.Div([
                     dcc.Graph(id='dem_rec', figure=demographics_received('data/template/'))
                     ]),
                ])

def tab2():
    return html.Div([
            div_statistics(),
            html.Div([
                     dcc.Graph(id='statistics', figure=statsPlot('data/template/', 'calls', 'heatmap'))
                     ])
            ])

def tab3():
    return html.Div([
                html.Div([
                        tab3_left()
                        ],style={'width': '22%', 'height': '800px', 'display':'inline-block', 
                    'backgroundColor': 'rgba(105, 105, 105, 0.2)', 'vertical-align': 'top'}),
                
                html.Div([
                        dcc.Graph(id='tempgraph', figure=transaction('data/template/')),
                        dcc.Graph(id='subgraph', figure=transaction('data/G1/'))
                        ],style={'width': '78%','display':'inline-block', 
                            'backgroundColor': 'rgba(15, 15, 105, 0.2)',
                            'text-align':'center', 'color': 'maroon',
                            'font-weight': 'bold'})
                    ])

def tab4():
    return html.Div([
                dcc.Tabs(id='subtabs', value='subtab-1', children=[
                    dcc.Tab(label='Transactions', value='subtab-1'),
                    dcc.Tab(label='Coauthorship', value='subtab-2'),
                    dcc.Tab(label='Procurement', value='subtab-3'),
                ]),
                html.Div(id='subtabs_content')
            ])

if __name__ == "__main__":
    tab1()
