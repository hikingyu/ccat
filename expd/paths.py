#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:54:41 2018
@author: hiking
"""
import networkx as nx
import cons.binance as cons
import itertools

'''
'''
symbols=cons.SYMBOLS
BASE_CURRENCIES=['BTC','ETH','USDT','BNB']
def symbols_currencies(symbols):#return list
    currencies=[]
    for symbol in symbols:
        base_currency, quote_currency = symbol.split('/')
        if base_currency not in currencies :currencies.append(base_currency)
        if quote_currency not in currencies :currencies.append(quote_currency)
    return currencies

def symbols_nodes(symbols):#return list
    nodes=[]
    for symbol in symbols:
        base_currency, quote_currency = symbol.split('/')
        if base_currency not in nodes:nodes.append(base_currency)
        if quote_currency not in nodes:nodes.append(quote_currency)
    return nodes

def symbols_slices(symbols):#return dict
    currencies=symbols_currencies(symbols)
    symbols_slices={}
    while currencies !=[]:
        currency=currencies.pop(0)
        s1=[]
        for symbol in symbols:
            if currency in symbol:s1.append(symbol)
        symbols_slices[currency]=s1   
    return symbols_slices

def edges_nodes(edges):
    nodes=[]
    for edge in edges:
        if edge[0] not in nodes:nodes.append(edge[0])
        if edge[1] not in nodes:nodes.append(edge[1])
    return nodes


def nodes_edges(nodes):
    edges=[]
    for i in nodes:
        for j in nodes:
            if i != j :edges.append((i,j))
    return edges

def symbols_edges(symbols):#return list
    edges=[]
    for symbol in symbols:
        base_currency, quote_currency = symbol.split('/')
        edges.append((base_currency, quote_currency))
        edges.append(( quote_currency,base_currency))    
    return edges

def edges_paths(edges):    #return list
    G = nx.DiGraph(edges)
    return list(nx.simple_cycles(G))

def edges_cycles(edges):
    cycles=[]
    nodes=edges_nodes(edges)
    num=len(nodes)
    for i in range(3,num+1):
        per=list(itertools.permutations(nodes,i))
        for j in per:
            path=[]
            for k in range(len(j)-1):
                if (j[k],j[k+1]) not in edges:
                    
                    break
                else:
                    path.append((j[k],j[k+1]))
            if (j[len(j)-1],j[0]) not in edges:
                break
            else:
                path.append((j[len(j)-1],j[0]))
            cycles.append(path)
    return cycles

def tickers_weight(tickers,fee):
    weights={}
    
    for symbol in tickers.keys():
        
        base_currency, quote_currency = symbol.split('/')
        ticker=tickers[symbol]
        ticker_bid = ticker['bid']
        ticker_ask = ticker['ask']
        bid_volume = ticker['bidVolume']
        ask_volume = ticker['askVolume']
        
        bid=ticker_bid*(1-fee)
        ask=1  if ticker_ask==0 else (1-fee)/ticker_ask
        value={}
        value['volume']=bid_volume
        value['weight']=bid
        weights[(base_currency,quote_currency)]=value
        value={}
        value['weight']=ask
        value['volume']=ask_volume   
        weights[(quote_currency,base_currency)]=value
    return weights

def cycles_weight(cycles,weights):
    cyclesweight={}
    for cycle in list(cycles.values()):
        weight=1
        for edge in cycle:
            if edge in list(weights.keys()):
                weight=weight*weights[edge]['weight']
            else:break;weight=1
        print((cycle),'--------')
        cyclesweight[(cycle)]=weight
    return cyclesweight
            
def paths_weights(paths,weights):
    paths_weights={}
    edges=paths_edges(paths)
    value=1
    for edge in edges:
        value=value*weights[edge]
    paths_weights['paths']=paths        
    paths_weights['weight']=value

    return paths_weights

def paths_edges(paths):
    edges=[]
    for i in range(len(paths)-1):
        edges.append((paths[i],paths[i+1])) 
    edges.append((paths[-1],paths[0]))   
    print(edges)
    return edges

def check_symbols_on_tickers(symbols,tickers):#return list
    
    return symbols

def check_nodes_on_tickers(nodes,tickers):#return list
    
    return nodes

if __name__ == '__main__':
    currencies=symbols_currencies(symbols)
    ss=symbols_slices(symbols)
    nodes=symbols_nodes(symbols)
    edges=symbols_edges(symbols)
    cycles={}
    '''
    for node in nodes:
        cycles[node]=ray.get(edges_cycles.remote(symbols_edges(ss[node])+nodes_edges(BASE_CURRENCIES)))
    '''
    node='ADA'
    cycles[node]=edges_cycles(symbols_edges(ss[node])+nodes_edges(BASE_CURRENCIES))
    