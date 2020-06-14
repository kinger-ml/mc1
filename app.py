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
from stats_plot import getStatsPlot

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs_top', value='tab-1', children=[
        dcc.Tab(label='Transactions', value='tab-1'),
        dcc.Tab(label='Stats and Demographics', value='tab-2'),
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
    
@app.callback([Output(component_id='seeds', component_property='style'),
              Output('transaction', 'figure'),
              Output('call_statistics', 'figure'),
              Output('email_statistics', 'figure')],
              [Input(component_id='graph_name', component_property='value')])

def show_hide_element(graph_value):
    if graph_value == 'data/large/':
        return {'height': '25px','width': '80%','display':'inline-block'}, transactions_graph('data/template/'), getStatsPlot('data/template/', 'calls')
    else:
        return {'display':'none'}, transactions_graph(graph_value), getStatsPlot(graph_value, 'calls'), getStatsPlot(graph_value, 'emails')

if __name__ == '__main__':
    app.run_server(debug=True)
