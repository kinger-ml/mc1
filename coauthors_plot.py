# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:46:42 2020

@author: Krishna Kinger
"""
import pandas as pd
import plotly.express as px
def coauthors_plot(path):
    if (path == 'data/G1/') or (path == 'data/G2/') or (path=='data/G3/'):
        df = pd.read_csv(path+'coauthors.csv')
        df['Time'] = pd.to_datetime(df['Time'])
        df['Source'] = 'Person: '+df['Source'].astype(str)
        df['Target'] = 'Document: '+df['Target'].astype(str)
        fig = px.sunburst(df, path=['Source','Time', 'Target'], values=df['Weight'])
        return fig
    else:
        data = dict(character=["No Coauthorship Data"], parent=[""], value=[0])
        fig =px.sunburst(data, names='character', parents='parent', values='value')
        return fig

def coauthors_datatable(nodetype, node):
    df = pd.read_csv('data/large/coauthors.csv')
    if nodetype == 'Person':
        df = df[df.Source == node]
    else:
        df = df[df.Target == node]
    columns=[{"name": i, "id": i} for i in df.columns]
    data=df.to_dict("rows")
    return data, columns
  
if __name__ == "__main__":
    coauthors_plot()
