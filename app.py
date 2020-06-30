# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:42:31 2020

@author: Krishna Kinger
"""
import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output
from tabs import tab1, tab2, tab3
from transaction_plot import transactions_graph
from stats_plot import statsPlot
from coauthors_plot import coauthors_plot
from demographics_plot import demographics_spent, demographics_received
from matching_plots import getGraph

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs_top', value='tab-1', children=[
        dcc.Tab(label='Transactions', value='tab-1'),
        dcc.Tab(label='Statistics', value='tab-2'),
        dcc.Tab(label='Pattern Matching', value='tab-3'),
    ]),
    html.Div(id='tabs_content')
])

@app.callback(Output('tabs_content', 'children'),
              [Input('tabs_top', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1()
    elif tab == 'tab-2':
        return tab2()
    elif tab == 'tab-3':
        return tab3()
    
@app.callback([Output('transaction', 'figure'),
              Output('coauthors', 'figure'),
              Output('dem_spend', 'figure'),
              Output('dem_rec', 'figure')],
              [Input(component_id='graph_name', component_property='value')])

def tab1_updates(graph_value):
    return transactions_graph(graph_value), coauthors_plot(graph_value), demographics_spent(graph_value), demographics_received(graph_value)


@app.callback(Output('statistics', 'figure'),
              [Input(component_id='graph_name2', component_property='value'),
               Input(component_id='channel', component_property='value'),
               Input(component_id='charts', component_property='value')])

def tab2_updates(graph_value, channel, charts):
    return statsPlot(graph_value, channel, charts)

@app.callback([Output('tempgraph', 'figure'),
               Output('subgraph', 'figure')],
              [Input(component_id='graph_name_match', component_property='value'),
               Input(component_id='chart_name_match', component_property='value')])

def tab3_updates(graph_value, charts):
    fig1 = getGraph('data/template/', charts)
    fig2 = getGraph(graph_value, charts)
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=False)
