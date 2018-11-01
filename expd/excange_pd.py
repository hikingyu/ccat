#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:51:29 2018

@author: hiking
"""

import pandas as pd
import ccxt
'''
class expd(ccxt):
    def __init__(self):
        pass
'''        
    

class exchang_pd(ccxt.Exchange):
    def __init__(self,exchange_id):
        #self.id=exchange_id
        self.exchang_pd =getattr(ccxt, exchange_id)()
        self.symbols_pd = self.exchang_pd.symbols
        return self.exchang_pd
    
    def load_markets_pd(self):
        self.markets_pd=self.exchange_pd.load_markets()
        
        return self.markets_pd
    
    def fetch_tickers_pd(self):
        self.tickers_pd = self.exchange_pd.fetch_tickers()
        return self.tickers_pd

def dict_pd(dict_data):
    index = list(dict_data.keys())
    data = list(dict_data.values())
    return pd.DataFrame(data,index)
