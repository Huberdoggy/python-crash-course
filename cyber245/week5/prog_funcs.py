from datetime import date, timedelta
import yahoo_fin.stock_info as si # this will allow us to retrieve the ACTUAL live prices

today = date.today()
format_today = today.strftime("%m/%d/%Y") # manipulate this to correctly pass to function will return table
# values in format xxxx/xx/xx
last_week = today - timedelta(days=7) # subtract from today and format as above
format_last_week = last_week.strftime("%m/%d/%Y")



def make_ticker_dict(raw_lst):
    real_ticker_data = {} # init empty list to hold key/vals of tickers and corresponding prices
    for ticker in sorted(raw_lst):
        try:
            real_ticker_data[ticker] = si.get_live_price(ticker)
        except Exception as ex: # Not sure what the exception will be so keep it open
            print(ex)
            continue # skip that ticker
    return real_ticker_data

def get_extended_ticker_data(ticker): # get data from the past week of the time the program is run
    ticker_table = si.get_data(ticker, start_date=format_last_week, end_date=format_today)
    return ticker_table