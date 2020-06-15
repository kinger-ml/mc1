# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:24:49 2020

@author: Krishna Kinger
"""
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
def getHeatmap(path, channel):
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

def getSunburst(path, channel, style):
    df = pd.read_csv(path+channel+'.csv')
    df['Time'] = pd.to_datetime(df['Time'])
    import calendar
    df['month'] = pd.DatetimeIndex(df['Time']).month
    df_new = df.groupby(['month','Source','Target']).size().reset_index().rename(columns={0:'count'})
    df_new['month'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    #fig1 = px.sunburst(df_new, path=['Source','month', 'Target'], values=df_new['count'], color='month',color_continuous_scale='RdBu')
    #fig2 = px.sunburst(df_new, path=['month','Source', 'Target'], values=df_new['count'], color='month',color_continuous_scale='RdBu')
    if style == 1:
        return px.sunburst(df_new, path=['Source','month', 'Target'], values=df_new['count'], color='month',color_continuous_scale='RdBu')
    else:
        return px.sunburst(df_new, path=['month','Source', 'Target'], values=df_new['count'], color='month',color_continuous_scale='RdBu')

def statsPlot(graph, channel, chart):
    if chart == 'heatmap':
        return getHeatmap(graph, channel)
    elif chart == 'sunburst1':
        return getSunburst(graph, channel, 1)
    else:
        return getSunburst(graph, channel, 2)
    
    
if __name__ == "__main__":
    getHeatmap()
