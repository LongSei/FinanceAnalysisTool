import yfinance as yf
import crawling.vnquant.data as vndt
import pandas as pd
from utils.function import *
import talib
class DataCrypto(): 
    def __init__(self, financeProduct: str) -> None:
        self.ticker = yf.Ticker(financeProduct)

    def getPrice(self): 
        result = self.getHistoricalData(period = '1d', interval = '1m')
        return [result['Close'][-1], result['Date'][-1]]

    def getInfo(self): 
        # Get information about the finance product (history)
        result = self.ticker.info
        print(result)

    def getHistoricalData(self, beginTime, endTime, interval = '1d'): 
        ''' 
        Usage
        -----
        Get the historical price of crypto product

        Parameters
        ----------
        beginTime (%YYYY/%mm/%dd): time begin crawling data
        endTime (%YYYY/%mm/%dd): time stop crawling data
        interval (string): interval between data (Ex: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo)

        Returns
        -------
        data (DataFrame): price of crypto product
        '''
        data = self.ticker.history(start=beginTime, end=endTime, interval=interval)

        # Insert date data into dataframe
        date = data.index
        date = [day.strftime("%H:%M:%S(UTC) - %d/%m/%Y") for day in date[0::].tolist()]
        idx = [x for x in range(1, len(data['Close']) + 1)]
        data.insert(loc=0, column='Index', value=idx)
        data.insert(loc=0, column='Date', value=date)
        data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        data = data.reset_index(drop=True)
        return data
    
    def getHolders(self): 
        # Get the information of the amount finance product the holders kept
        InstitutionalHolders = self.ticker.institutional_holders
        MajorHolders = self.ticker.major_holders
        MutualFundHolders = self.ticker.mutualfund_holders
        return (InstitutionalHolders, MajorHolders, MutualFundHolders)
    
class DataStock(): 
    def __init__(self, financeProduct: str) -> None:
        self.StockTicker = vndt.DataLoader(symbols=financeProduct, start='2018-01-01', end='2018-01-01', data_source='vnd')
        self.CompanyTicker = vndt.FinanceLoader(symbol=financeProduct, start='2018-01-01', end='2018-01-01')
    
    def getHistoricalData(self, beginTime=None, endTime=None):
        ''' 
        Usage
        -----
        Get the historical price of stock

        Parameters
        ----------
        beginTime (%YYYY/%mm/%dd): time begin crawling data
        endTime (%YYYY/%mm/%dd): time stop crawling data

        Returns
        -------
        data (DataFrame): price of stock product
        '''
        self.StockTicker.start = beginTime = self.StockTicker.start if beginTime == None else beginTime
        self.StockTicker.end = endTime = self.StockTicker.end if endTime == None else endTime
        data = self.StockTicker.download()

        # Flatten the columns of dataFrame
        data.columns = data.columns.get_level_values(0)

        # Add Date for DataFrame
        date = data.index
        date = [day.strftime("%Y-%m-%d") for day in date[0::].tolist()]
        data['Date'] = date
        for key in data.keys():
            data[key[0].upper() + key[1:]] = data[key]
        data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        data = data.reset_index(drop=True)
        return data
    
    def getBasicIndex(self, beginTime=None, endTime=None):
        '''
        Usage
        -----
        Get the index (ROA, ROE, Net Profit Marget, Net Revenue Growth, Profit After tax Growth) of company 

        Parameters
        ----------
        beginTime (%YYYY/%mm/%dd): time begin crawling data
        endTime (%YYYY/%mm/%dd): time stop crawling data

        Returns
        -------
        data (DataFrame): index of company
        '''
        self.CompanyTicker.start = beginTime = self.CompanyTicker.start if beginTime == None else beginTime
        self.CompanyTicker.end = endTime = self.CompanyTicker.end if endTime == None else endTime
        data = self.CompanyTicker.get_basic_index()
        return data

class AddAttribute(): 
    def SMA(self, priceData, timePeriod, priceName, columnName): 
        '''
        Usage
        -----
        Add SMA column to DataFrame

        Parameters
        ----------
        priceData (DataFrame): the dataframe you base on
        timePeriod (int): interval for each data record
        priceName (str): the name of the column you want to base on
        columnName (str): the name of the column you want to add

        Returns
        -------
        priceData (DataFrame): Dataframe have SMA
        '''

        priceData[columnName] = talib.SMA(priceData[priceName], timeperiod=timePeriod)
        return priceData
    
    def RSI(self, priceData, timePeriod, priceName, columnName): 
        '''
        Usage
        -----
        Add RSI column to DataFrame

        Parameters
        ----------
        priceData (DataFrame): the dataframe you base on
        timePeriod (int): interval for each data record
        priceName (str): the name of the column you want to base on
        columnName (str): the name of the column you want to add

        Returns
        -------
        priceData (DataFrame): Dataframe have RSI
        '''
        priceData[columnName] = talib.RSI(priceData[priceName], timeperiod=timePeriod)
        return priceData
    
    def BBANDS(self, priceData, timePeriod, priceName, columnName): 
        '''
        Usage
        -----
        Add Bollinger Bands column to DataFrame

        Parameters
        ----------
        priceData (DataFrame): the dataframe you base on
        timePeriod (int): interval for each data record
        priceName (str): the name of the column you want to base on
        columnName (str): the name of the column you want to add

        Returns
        -------
        priceData (DataFrame): Dataframe have Bollinger Bands
        '''
        upper, middle, lower = talib.BBANDS(priceData[priceName], timeperiod=timePeriod)

        priceData[columnName] = [[upper[idx], middle[idx], lower[idx]] for idx in range(len(upper))]
        return priceData
