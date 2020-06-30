# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:21:44 2020

@author: Krishna Kinger
"""
from transaction_plot import transactions_graph
from stats_plot import statsPlot
from coauthors_plot import coauthors_plot
from demographics_plot import demographics_spent, demographics_received

def transaction(path):
    fig = transactions_graph(path)
    fig.update_xaxes(rangeslider_visible=False)
    fig.update_layout(
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
    return fig
    
def getGraph(path, chart):
    channel, charttype='', ''
    if chart == 'transactions':
        return transaction(path)
    elif chart == 'coauthorship':
        return coauthors_plot(path)
    elif chart == 'demographicsS':
        return demographics_spent(path)
    elif chart == 'demographicsR':
        return demographics_received(path)
    else:
        if 'call' in chart:
            channel = 'calls'
        elif 'email' in chart:
            channel = 'emails'
        else:
            channel = 'travels'
        
        if 'heatmap' in chart:
            charttype = 'heatmap'
        elif 'sunburst1' in chart:
            charttype = 'sunburst1'
        elif 'sunburst2' in chart:
            charttype = 'sunburst2'
        elif 'sunburst3' in chart:
            charttype = 'sunburst3'
        return statsPlot(path, channel, charttype)
            
    
if __name__ == "__main__":
    pass
