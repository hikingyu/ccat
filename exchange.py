# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ccxt

exchange_id='binance'
exchange = getattr(ccxt, exchange_id)()
marks= exchange.load_markets()              #get

currency = exchange.currencies              #货币列表
symbols = exchange.symbols                  #获取符号列表
fees = exchange.fees  
fee = fees['trading']['maker']
tickers = exchange.fetch_tickers()


