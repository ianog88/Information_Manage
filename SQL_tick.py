from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import datetime as dt
import threading
import sqlite3


class TradeApp(EWrapper, EClient): 
    def __init__(self): 
        EClient.__init__(self, self) 

    def tickByTickAllLast(self, reqId, tickType, time, price, size, tickAtrribLast, exchange, specialConditions):
        super().tickByTickAllLast(reqId, tickType, time, price, size, tickAtrribLast, exchange, specialConditions)
        if tickType == 1:
            pass
        else:
            c=db.cursor()
            for ms in range(100):
                try:
                    print(" ReqId:", reqId, "Time:", (dt.datetime.fromtimestamp(time)+dt.timedelta(milliseconds=ms)).strftime("%Y%m%d %H:%M:%S.%f"), "Price:", price, "Size:", size)
                    vals = [(dt.datetime.fromtimestamp(time)+dt.timedelta(milliseconds=ms)).strftime("%Y%m%d %H:%M:%S.%f"),price, size]
                    query = "INSERT INTO TICKER{}(time,price,volume) VALUES (?,?,?)".format(reqId)
                    c.execute(query,vals)
                    break
                except Exception as e:
                    print(e)
        try:
            db.commit()
        except:
            db.rollback()
        

def usTechStk(symbol,sec_type="STK",currency="USD",exchange="ISLAND"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract 


def streamData(req_num,contract):
    app.reqTickByTickData(reqId=req_num, 
                          contract=contract,
                          tickType="AllLast",
                          numberOfTicks=0,
                          ignoreSize=True)
    
def websocket_con(tickers):
    global db
    db = sqlite3.connect('**filepath**/ticks.db') 
    c=db.cursor()
    for i in range(len(tickers)):
        c.execute("CREATE TABLE IF NOT EXISTS TICKER{} (time datetime primary key,price real(15,5), volume integer)".format(i))
    try:
        db.commit()
    except:
        db.rollback()
    app.run()

tickers = ['MMM', 'AOS', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADM', 'ADBE', 'ADP', 'AAP', 'AES', 'AFL', 'A', 'AIG', 'APD',
'AKAM', 'ALK', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AMD', 'AEE',
'AAL', 'AEP', 'AXP', 'AMT', 'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM', 'AON', 'APA', 'AAPL',
'AMAT', 'APTV', 'ANET', 'AIZ', 'T', 'ATO', 'ADSK', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC', 'BBWI', 'BAX', 'BDX',
'WRB', 'BRK.B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR',
'BRO', 'BF.B', 'CHRW', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE',
'CBRE', 'CDW', 'CE', 'CNC', 'CNP', 'CDAY', 'CERN', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI',
'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CTXS', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG',
'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CTVA', 'COST', 'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI']

app = TradeApp()
app.connect(host='127.0.0.1', port=0000, clientId=00)
con_thread = threading.Thread(target=websocket_con, args=(tickers,), daemon=True)
con_thread.start()

for ticker in tickers:
    streamData(tickers.index(ticker),usTechStk(ticker))