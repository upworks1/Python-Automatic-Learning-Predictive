ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='DAI', interval = '1min', outputsize = 'compact')

with open('Mercedes-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


Crypto = CryptoCurrencies(key=api_key, output_format="csv",)
data, meta_data = Crypto.get_digital_currency_daily(symbol='ETH', market="USD" )

with open('Eth-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row)



ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='GOLD', interval = '1min', outputsize = 'compact')

with open('gold-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in reader:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='NKE', interval = '1min', outputsize = 'compact')

with open('Nike-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='NDAQ', interval = '1min', outputsize = 'compact')

with open('Nsdq-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='NVDA', interval = '1min', outputsize = 'compact')

with open('Nvidia-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 



ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='WTI', interval = '1min', outputsize = 'compact')

with open('oil-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row)


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='UG', interval = '1min', outputsize = 'compact')

with open('Peugeot-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='TSLA', interval = '1min', outputsize = 'compact')

with open('tesla-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='UBER', interval = '1min', outputsize = 'compact')

with open('Uber-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 


ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='SPCE', interval = '1min', outputsize = 'compact')

with open('VirginGalactic-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 



ts = TimeSeries(key=api_key, output_format="csv")
data, meta_data = ts.get_intraday(symbol='BHC', interval = '1min', outputsize = 'compact')

with open('Valeant-realtime.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data:
       try: 
           reader = csv.reader(write_csvfile)
           for r in data:
               reader.writerow(row[r])
           
       except:
         writer.writerow(row) 