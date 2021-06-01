import time 
from luno_python.client import Client

def main():
  period = 1
  pair='XBTZAR'

  conn = Client(api_key_id='', 
                api_key_secret='')
  while True:
    try:
      res = conn.get_ticker(pair)
      lastPairPrice = ticker['ask']
      dateTime = datetime.datetime.now().time().strftime('%Y-%m-%d %H:%M:%S')
      
      print('%s %s - ASK: %s\tBID %s' % 
           (dateTime, pair, lastPairPrice, ticker['bid']))
    
    except Exception as e:
      print(e)
    
    time.sleep(period)

if __name__ == '__main__':
  main()