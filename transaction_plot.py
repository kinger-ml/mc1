# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:10:03 2020

@author: Krishna Kinger
"""
import pandas as pd
from collections import Counter
import datetime
import plotly.graph_objects as go
def add_time(dt, duration):
    return (dt+ datetime.timedelta(0,86400*int(duration)))
    
def SetColor(x):
    if(x == 0):
        return '#636EFA'
    elif(x == 1):
        return '#EF553B'
    elif(x == 2):
        return '#00CC96'
    elif(x == 3):
        return '#AB63FA'
    elif(x == 4):
        return '#19D3F3'
    elif(x == 5):
        return '#AA0DFE'
    else:
        return "black"

def transactions_graph(path):
    df_calls = pd.read_csv(path+"calls.csv")
    df_emails = pd.read_csv(path+"emails.csv")
    df_travels = pd.read_csv(path+"travel.csv")
    df_location = pd.read_csv(path+"location.csv")
    
    df_sale = pd.read_csv(path+"sale.csv")
    df_purchase = pd.read_csv(path+"purchase.csv")
    df_sale = df_sale.rename(columns={"Target": "Item"})
    df_purchase = df_purchase.rename(columns={"Target": "Item", "Source":"Target"})
    df_procurement = pd.merge(df_sale, df_purchase,  how='left', left_on=['Weight','Time', 'Item'], right_on = ['Weight','Time', 'Item'])
    
    
    df_calls['Time'] = pd.to_datetime(df_calls['Time'])
    df_emails['Time'] = pd.to_datetime(df_emails['Time'])
    df_travels['Time'] = pd.to_datetime(df_travels['Time'])
    df_location['Time'] = pd.to_datetime(df_location['Time'])
    
    df_procurement['Time'] = pd.to_datetime(df_procurement['Time'])
    
    
    persons = df_calls['Source'].tolist()
    persons.extend(df_calls['Target'].tolist())
    
    persons.extend(df_emails['Source'].tolist())
    persons.extend(df_emails['Target'].tolist())
    
    persons.extend(df_travels['Source'].tolist())
    
    persons.extend(df_procurement['Source'].tolist())
    persons.extend(df_procurement['Target'].tolist())
    persons.sort(key=Counter(persons).get, reverse=False)
    
    
    
    
    tim_calls, ys_calls = [], []
    tim_emails, ys_emails = [], []
    tim_travel, yt = [], []
    time_list_t = []
    time_procurement, yp= [],[]
    for i in range(len(df_calls['Time'])):
        tim_calls.append(df_calls['Time'][i])
        tim_calls.append(df_calls['Time'][i])
        tim_calls.append(df_calls['Time'][i])
        ys_calls.append(df_calls['Source'][i])
        ys_calls.append(df_calls['Target'][i])
        ys_calls.append(None)
    for i in range(len(df_emails)):    
        tim_emails.append(df_emails['Time'][i])
        tim_emails.append(df_emails['Time'][i])
        tim_emails.append(df_emails['Time'][i])
        ys_emails.append(df_emails['Source'][i])
        ys_emails.append(df_emails['Target'][i])
        ys_emails.append(None)
    for i in range(len(df_travels['Source'])):
        tim_travel.append(df_travels['Time'][i])
        temp = add_time(df_travels['Time'][i], df_travels['Weight'][i])
        tim_travel.append(temp)
        time_list_t.append(temp)
        tim_travel.append(None)
        yt.append(df_travels['Source'][i])
        yt.append(df_travels['Source'][i])
        yt.append(None)
    for i in range(len(df_procurement['Time'])):
        time_procurement.append(df_procurement['Time'][i])
        time_procurement.append(df_procurement['Time'][i])
        time_procurement.append(None)
        yp.append(df_procurement['Source'][i])
        yp.append(df_procurement['Target'][i])
        yp.append(None)
        
    df_location['Time'] = pd.to_datetime(df_location['Time'])
    df_source = pd.merge(df_calls, df_location,  how='left', left_on=['Source','Time'], right_on = ['Source','Time'])
    df_target = pd.merge(df_calls, df_location,  how='left', left_on=['Target','Time'], right_on = ['Source','Time'])
    src_locations_calls = df_source['Location'].tolist()
    tgt_locations_calls = df_target['Location'].tolist()
    
    df_source = pd.merge(df_emails, df_location,  how='left', left_on=['Source','Time'], right_on = ['Source','Time'])
    df_target = pd.merge(df_emails, df_location,  how='left', left_on=['Target','Time'], right_on = ['Source','Time'])
    src_locations_emails = df_source['Location'].tolist()
    tgt_locations_emails = df_target['Location'].tolist()
    
    df_source = pd.merge(df_travels, df_location,  how='left', left_on=['Source','Time'], right_on = ['Source','Time'])
    src_locations_travel = df_source['Location'].tolist()
    tgt_locations_travel = df_travels['TargetLocation'].tolist()
    
    locations_proc= [6] * len(df_procurement['Source'])
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = tim_calls, y = ys_calls, opacity = 0.5,legendgroup="Calls", name='Calls', line=dict(color='red', width=1)))
    fig.add_trace(go.Scatter(x=df_calls['Time'], y= df_calls['Source'],opacity = 0.5, legendgroup="Calls", name='Source', mode='markers', marker_symbol=100, marker=dict(color=list(map(SetColor, src_locations_calls)),size=5)))
    fig.add_trace(go.Scatter(x=df_calls['Time'], y= df_calls['Target'],opacity = 0.5, legendgroup="Calls", name='Target', mode='markers', marker_symbol=11, marker=dict(color=list(map(SetColor, tgt_locations_calls)),size=5)))
    
    fig.add_trace(go.Scatter(x = tim_emails, y = ys_emails,opacity = 0.5, legendgroup="Emails", name='Emails', line=dict(color='green', width=1)))
    fig.add_trace(go.Scatter(x=df_emails['Time'],opacity = 0.5, y= df_emails['Source'], legendgroup="Emails", name='Source', mode='markers', marker_symbol=100, marker=dict(color=list(map(SetColor, src_locations_emails)),size=5)))
    fig.add_trace(go.Scatter(x=df_emails['Time'],opacity = 0.5, y= df_emails['Target'], legendgroup="Emails", name='Target', mode='markers', marker_symbol=11, marker=dict(color=list(map(SetColor, tgt_locations_emails)),size=5)))
    
    fig.add_trace(go.Scatter(x = tim_travel, y = yt,opacity = 0.5, legendgroup="Travel", name='Travel', line=dict(color='blue', width=3)))
    fig.add_trace(go.Scatter(x=df_travels['Time'],opacity = 0.8, y= df_travels['Source'], legendgroup="Travel", name='Source', mode='markers', marker_symbol=0, marker=dict(color=list(map(SetColor, src_locations_travel)),size=5)))
    fig.add_trace(go.Scatter(x=time_list_t,opacity = 0.8, y= df_travels['Source'], legendgroup="Travel", name='Destination', mode='markers', marker_symbol=11, marker=dict(color=list(map(SetColor, tgt_locations_travel)),size=5)))
    
    fig.add_trace(go.Scatter(x = time_procurement, y = yp, opacity = 0.8,legendgroup="Procurement", name='Procurement', line=dict(color='plum', width=5)))
    fig.add_trace(go.Scatter(x=df_procurement['Time'], y= df_procurement['Source'],opacity = 0.5, legendgroup="Procurement", name='Seller', mode='markers', marker_symbol=100, marker=dict(color=list(map(SetColor, locations_proc)),size=5)))
    fig.add_trace(go.Scatter(x=df_procurement['Time'], y= df_procurement['Target'],opacity = 0.5, legendgroup="Procurement", name='Buyer', mode='markers', marker_symbol=11, marker=dict(color=list(map(SetColor, locations_proc)),size=5)))
    
    
    fig.update_layout(
            legend_orientation="h",
        yaxis = dict(
            type = 'category',
            categoryarray= persons
        ),
        xaxis = dict(
            side='top'
        ),
        height=800
    )
    fig.update_xaxes(rangeslider_visible=True)
    return fig

if __name__ == "__main__":
    transactions_graph('path')
