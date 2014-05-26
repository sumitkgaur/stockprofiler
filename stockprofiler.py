import requests
import json
import urllib
from datetime import datetime
from pprint import pprint
 
now = datetime.now()
print "-" * 30
print "WELCOME"
print str(now)
print "-" * 30

# Get the feed
url = 'http://query.yahooapis.com/v1/public/yql';
startDate = '2012-01-01';
endDate = '2012-02-01';

#historical data	
data1 = urllib.quote('select * from yahoo.finance.historicaldata where symbol in ("ACC","ABB") and startDate = "' + startDate + '" and endDate = "' + endDate + '"', safe='~()*!.\'')

#symbol search
#data2 = urllib.quote('select symbol,LastTradeWithTime from yahoo.finance.quotes where symbol in ("ACC","ABB")', safe='~()*!.\'')
data2 = urllib.quote('select * from yahoo.finance.quotes where symbol in ("ACC","ABB")', safe='~()*!.\'')

finalurl = url+'?q='+data2+"&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"

r = requests.get(finalurl)
r.text
# Convert it to a Python dictionary
data = json.loads(r.text)
#print r.text
pprint(data)

for entry in data['query']['results']['quote']:
    print entry['symbol']
    print entry['LastTradeWithTime']
    print entry['DaysRange']
    print entry['YearLow']
    print entry['YearHigh']
