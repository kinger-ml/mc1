# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:42:31 2020

@author: Krishna Kinger
"""
import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State
from tabs import tab1, tab2, tab3, tab4
from transaction_plot import transactions_graph
from stats_plot import statsPlot
from coauthors_plot import coauthors_plot, coauthors_datatable
from demographics_plot import demographics_spent, demographics_received
from matching_plots import getGraph
from subtabs import subtab1, subtab2, subtab3
from process_transactions import getRelatedPeople, getTransactions
from largegraph import transactions_graph_large, procurement_large

import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('data/large/coauthors.csv')
persons = df['Source'].tolist()
persons = sorted(list(set(persons)))
documents = df['Target'].tolist()
documents = sorted(list(set(documents)))
dropdown_dict = {'Person': persons, 'Document':documents}
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id='tabs_top', value='tab-1', children=[
        dcc.Tab(label='Transactions', value='tab-1'),
        dcc.Tab(label='Statistics', value='tab-2'),
        dcc.Tab(label='Pattern Matching', value='tab-3'),
        dcc.Tab(label='Large Graph', value='tab-4'),
    ], style={'font-weight':'bold', 'backgroundColor': 'rgba(15, 15, 105, 0.2)',
              'fontSize': '20', 'font-family':'sans-serif'}),
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
    elif tab == 'tab-4':
        return tab4()
    
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
               Input(component_id='chart_name_match', component_property='value'),
               Input('reorder_nodes_template', 'n_clicks'),
               Input('reorder_nodes_subgraph', 'n_clicks')],
               [State('nodes_order_template', 'value'),
               State('nodes_order_subgraph', 'value')])
def tab3_updates(graph_value, charts, btn1, btn2, temp_order, sub_order):
    fig1 = getGraph('data/template/', charts)
    fig2 = getGraph(graph_value, charts)
    if charts!='transactions':
        return fig1, fig2
    #Handling only for transactions
    ctx = dash.callback_context
    if not ctx.triggered:
        return fig1, fig2
    else:
        persons1, persons2 = [], []
        if temp_order!=None:
            persons1 = [int(s) for s in temp_order.split(',')]
            fig1.update_layout(
                yaxis = dict(
                        type = 'category',
                        categoryarray= persons1
                        ))
        if sub_order!=None:
            persons2 = [int(s) for s in sub_order.split(',')]
            fig2.update_layout(
                yaxis = dict(
                        type = 'category',
                        categoryarray= persons2
                        ))
        return fig1, fig2

@app.callback(Output('subtabs_content', 'children'),
              [Input('subtabs', 'value')])
def render_subtabs(subtab):
    if subtab == 'subtab-1':
        return subtab1()
    elif subtab == 'subtab-2':
        return subtab2()
    elif subtab == 'subtab-3':
        return subtab3()
    elif subtab == 'subtab-4':
        return tab3()

@app.callback(Output('out_seed', 'value'),
              [Input('fetchNodes', 'n_clicks')],
              [State('inp_seed', 'value')])
def update_nodes(n_clicks, value):
    if n_clicks!=None:
        seeds = [int(s) for s in value.split(',')]
        print(seeds)
        persons = getRelatedPeople(seeds)
        persons = str(persons)
        persons = persons.replace("[", "")
        persons = persons.replace("]", "")
        return str(persons)

@app.callback(Output('large_transactions', 'figure'),
              [Input('fetchTransactions', 'n_clicks'),
               Input('reorder_nodes', 'n_clicks')],
              [State('out_seed', 'value'),
               State('nodes_order', 'value'),])
def fetch_transactions(btn1, btn2, out_seeds, nodes_order):
    ctx = dash.callback_context
    if not ctx.triggered:
        print('Initial')
        return transactions_graph_large([])
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        print(button_id)
        if button_id == 'fetchTransactions':
            seeds = [int(s) for s in out_seeds.split(',')]
            getTransactions(seeds)
            print('updating graph')
            return transactions_graph_large(seeds)
        elif button_id == 'reorder_nodes':
            persons = [int(s) for s in nodes_order.split(',')]
            print(persons)
            fig = transactions_graph_large([])
            fig.update_layout(
                    yaxis = dict(
                            type = 'category',
                            categoryarray= persons
                            ))
            return fig

@app.callback(Output('node', 'options'),
              [Input('nodetype', 'value')])
def update_nodes_dropdown(name):
    return [{'label': i, 'value': i} for i in dropdown_dict[name]]

@app.callback([Output('coauthors_table', 'data'),
               Output('coauthors_table', 'columns')],
              [Input('nodetype', 'value'),
               Input('node', 'value'),])
def update_coauthors_datatable(nodetype, node):
    return coauthors_datatable(nodetype, node)

@app.callback(Output('procurement', 'figure'),
              [Input('item_node', 'value')])
def update_procurement(item):
    return procurement_large(item)

if __name__ == '__main__':
    app.run_server(debug=False)
