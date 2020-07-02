# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:29:45 2020

@author: Krishna Kinger
"""
import pandas as pd
from collections import Counter
def getemails(persons):
    df_emails = pd.DataFrame()
    persons = pd.Series(persons)
    for month in range(1, 13):
        print('Processed Emails for month',month)
        filename = 'data/large/emails/month_'+str(month)+'.csv'
        df = pd.read_csv(filename)
        drop_cols = ['SourceLocation', 'TargetLocation', 'SourceLatitude',
                     'SourceLongitude', 'TargetLatitude', 'TargetLongitude']
        df = df.drop(drop_cols, axis=1)
        df =df[df.Source.isin(persons) & df.Target.isin(persons)]
        df_emails = df_emails.append(df)
    df_emails.to_csv('data/large/processed/emails.csv', index=False)

def getcalls(persons):
    df_calls = pd.DataFrame()
    persons = pd.Series(persons)
    for month in range(1, 13):
        print('Processed Calls for month',month)
        filename = 'data/large/calls/month_'+str(month)+'.csv'
        df = pd.read_csv(filename)
        df =df[df.Source.isin(persons) & df.Target.isin(persons)]
        #add code to process location also
        drop_cols = ['SourceLocation', 'TargetLocation', 'SourceLatitude',
                     'SourceLongitude', 'TargetLatitude', 'TargetLongitude']
        df = df.drop(drop_cols, axis=1)
        df_calls = df_calls.append(df)
    df_calls.to_csv('data/large/processed/calls.csv', index=False)

def getProcurements(persons):
    df_sale = pd.read_csv('data/large/sales.csv')
    df_sale = df_sale[df_sale.Source.isin(persons)]
    df_purchase = pd.read_csv('data/large/purchase.csv')
    df_purchase = df_purchase[df_purchase.Source.isin(persons)]
    df_sale = df_sale.rename(columns={"Target": "Item"})
    df_purchase = df_purchase.rename(columns={"Target": "Item", "Source":"Target"})
    df_procurement = pd.merge(df_sale, df_purchase,  how='inner', left_on=['Weight','Time', 'Item'], right_on = ['Weight','Time', 'Item'])
    df_procurement.to_csv('data/large/processed/procurement.csv')

def getTravel(persons):
    df_result = pd.DataFrame()
    df_travels = pd.read_csv('data/large/travels0.csv')
    df_travels = df_travels[df_travels.Source.isin(persons)]
    df_travels = df_travels[df_travels.Weight > 0]
    drop_cols = ['SourceLocation', 'Target', 'SourceLatitude',
                     'SourceLongitude', 'TargetLatitude', 'TargetLongitude']
    df_travels = df_travels.drop(drop_cols, axis=1)
    df_result = df_result.append(df_travels)
    df_travels = pd.read_csv('data/large/travels1.csv')
    df_travels = df_travels[df_travels.Source.isin(persons)]
    df_travels = df_travels[df_travels.Weight > 0]
    drop_cols = ['SourceLocation', 'Target', 'SourceLatitude',
                     'SourceLongitude', 'TargetLatitude', 'TargetLongitude']
    df_travels = df_travels.drop(drop_cols, axis=1)
    df_result = df_result.append(df_travels)
    df_result.to_csv('data/large/processed/travels.csv', index=False)
    
    
def getTransactions(persons):
    getemails(persons)
    print('emails stored')
    getcalls(persons)
    print('calls stored')
    getProcurements(persons)
    print('Procurement Stored')
    
def getRelatedPeople(seed):
    persons = []
    seed = pd.Series(seed)
    for month in range(1, 13):
        print(month)
        filename = 'data/large/calls/month_'+str(month)+'.csv'
        df = pd.read_csv(filename)
        drop_cols = ['SourceLocation', 'TargetLocation', 'SourceLatitude',
                     'SourceLongitude', 'TargetLatitude', 'TargetLongitude']
        df = df.drop(drop_cols, axis=1)
        df =df[df.Source.isin(seed) | df.Target.isin(seed)]
        persons.extend(df.Source)
        persons.extend(df.Target)
        filename = 'data/large/emails/month_'+str(month)+'.csv'
        df = pd.read_csv(filename)
        drop_cols = ['SourceLocation', 'TargetLocation', 'SourceLatitude',
                     'SourceLongitude', 'TargetLatitude', 'TargetLongitude']
        df = df.drop(drop_cols, axis=1)
        df =df[df.Source.isin(seed) | df.Target.isin(seed)]
        persons.extend(df.Source)
        persons.extend(df.Target)
        for item in seed:
            persons = list(filter((item).__ne__, persons))
    c = Counter(persons)
    result = c.most_common(100)
    p = [r[0] for r in result]
    persons = []
    persons.extend(seed)
    persons.extend(p)
    return persons
    
if __name__ == "__main__":
    """
    seed = [600971, 611692, 540660, 609913, 470085, 484189, 612711, 602794, 554368]
    persons = getRelatedPeople(seed)
    c = Counter(persons)
    result = c.most_common(20)
    p = [r[0] for r in result]
    persons = []
    persons.extend(seed)
    persons.extend(p)
    #persons = [600971, 611692, 540660, 609913, 470085, 484189, 612711, 602794, 554368]
    t1 = time.clock()
    df_emails = getemails(persons)
    t2 = time.clock()
    print(t2-t1)
    t1 = time.clock()
    df_calls = getcalls(persons)
    t2 = time.clock()
    print(t2-t1)
    """
    persons = [550287, 512397, 635665, 640254, 524464, 571682, 602794, 537976, 570672, 601595, 653288, 561347, 557816, 578507, 483622, 631903, 554368, 463273, 613859, 508192, 613916, 599483, 529585, 527004, 480601, 487003, 647035, 488473, 496276, 637482, 650911, 606000, 534946, 605676, 544915, 596646, 476189, 498136, 549335, 635766, 623415, 504745, 482001, 560630, 500716, 520138, 554256, 622052, 581357, 640435, 552643, 564629]
    getTravel(persons)
