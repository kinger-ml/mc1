# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 14:37:24 2020

@author: Krishna Kinger
"""
import plotly.graph_objects as go
import pandas as pd
import plotly.figure_factory as ff
def df_to_plotly(df):
    persons = [str(item) for item in df.index.tolist()]
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': persons}
    
def demographics_spent(path):
    df_spend= pd.read_csv(path + 'demoS.csv', index_col = 0)
    persons = [str(item) for item in df_spend.index.tolist()]
    fig = go.Figure(data=go.Heatmap(df_to_plotly(df_spend)))
    fig.update_layout(
        title_text='Heatmap - Spendings',title_x=0.5, title_y = 1,
        xaxis = dict(
            type = 'category',
            categoryarray= df_spend.columns.tolist(),
            tickangle= 35
        ),
        yaxis = dict(
            type = 'category',
            showticklabels= True,
            categoryarray= persons
        ),
        height = 1000,
        yaxis_title="Person",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    return fig

def demographics_received(path):
    df= pd.read_csv(path+'demoR.csv', index_col = 0)
    df = df.fillna(0)
    colorscale=[[0.0, 'rgb(250,250,250)'],
            [0.1, 'rgb(10,250,250)'],
            [0.2, 'rgb(0,250,250)'],
            [0.3, 'rgb(0,200,250)'],
            [0.4, 'rgb(0,150,250)'],
            [0.5, 'rgb(0,100,250)'],
            [0.6, 'rgb(0,50,250)'],
            [0.7, 'rgb(0,0,250)'],
            [0.8, 'rgb(0,0,200)'],
            [0.9, 'rgb(0,0,100)'],
            [1.0, 'rgb(0,0,50)']]
    fig = ff.create_annotated_heatmap(z=df.values.tolist(), x = df.columns.tolist(), y = df.index.tolist())
    fig.update_layout(
        title_text='Heatmap-Earnings',title_x=0.5, title_y = 1,
        height=900,
        yaxis = dict(
            type = 'category',
            categoryarray= df.index.tolist()
        ),
        xaxis = dict(
            type = 'category',
            categoryarray= df.columns.tolist()
        ),
        yaxis_title="Person",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    return fig

if __name__ == "__main__":
    demographics_spent()
