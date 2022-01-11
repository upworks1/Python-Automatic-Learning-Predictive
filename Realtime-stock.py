import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.sectorperformance import SectorPerformances
import time
import csv

api_key = "B8DW82ILR50FH532"

ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_quote_endpoint(symbol='AMD')

with open('AMD-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row)
 



acb = TimeSeries(key=api_key, output_format="csv")
data, meta_data = acb.get_monthly(symbol='AMD')

with open('Training-data/AMD_train_year.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row)



Crypto = CryptoCurrencies(key=api_key, output_format="csv",)
data, meta_data = Crypto.get_digital_currency_daily(symbol='BTC', market="USD" )

with open('Btc-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row)


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_monthly(symbol='AAPL')

with open('Training-data/Apple_train_year.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row)  




