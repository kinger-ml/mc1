# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:24:49 2020

@author: Krishna Kinger
"""
import pandas as pd
import plotly.figure_factory as ff
def getStatsPlot(path, channel):
    df = pd.read_csv(path+'stats/'+ channel +".csv", index_col = 0)
    df = df[(df.T != 0).any()]
    df = df.loc[:, (df != 0).any(axis=0)]
    fig = ff.create_annotated_heatmap(z=df.values.tolist(), x = df.columns.tolist(), y = df.index.tolist())
    title = 'Heatmap - ' + channel.capitalize() + ' Data'
    fig.update_layout(
        title_text=title,title_x=0.5, title_y = 1,
        yaxis = dict(
            type = 'category',
            categoryarray= df.index.tolist()
        ),
        xaxis = dict(
            type = 'category',
            categoryarray= df.columns.tolist()
        ),
        height=600,
        xaxis_title="(Target)",
        yaxis_title="(Source)",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )
    return fig

if __name__ == "__main__":
    getStatsPlot()
