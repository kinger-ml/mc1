# -*- coding: utf-8 -*-
"""
Created on Mon May 25 19:59:10 2020

@author: Krishna Kinger
"""
import dash_html_components as html
import dash_core_components as dcc
from transaction_plot import transactions_graph
from assets.html_components import dropdown_graphs, dropdown_seeds, div_transactions, div_statistics
from stats_plot import getStatsPlot
def tab1():
    return html.Div([
                div_transactions(),
                html.Div([
                     dcc.Graph(id='transaction', figure=transactions_graph('data/template/'))
                     ]),
                div_statistics(),
                html.Div([
                     dcc.Graph(id='call_statistics', figure=getStatsPlot('data/template/', 'calls'))
                     ]),
                html.Div([
                     dcc.Graph(id='email_statistics', figure=getStatsPlot('data/template/', 'emails'))
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
