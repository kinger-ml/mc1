# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:59:10 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc
from transaction_plot import transactions_graph
from assets.html_components import div_transactions, div_coauthors, div_demographics
from assets.html_components import div_statistics
from coauthors_plot import coauthors_plot
from stats_plot import statsPlot
from demographics_plot import demographics_spent, demographics_received
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
