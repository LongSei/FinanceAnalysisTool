import yfinance as yf
class DataGetting(): 
    def __init__(self, financeProduct: str) -> None:
        self.main = yf.Ticker(financeProduct)

    def getPrice(self): 
        result = self.getHistoricalData(period = '1d', interval = '1m')
        return [result['Close'][-1], result['Date'][-1]]

    def getInfo(self): 
        # Get information about the finance product (history)
        result = self.main.info
        print(result)

    def getHistoricalData(self, period = '1mo', interval = '1d'): 
        # Get the dataframe about Finance Product
        # ['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits', 'Capital Gains']
        result = self.main.history(period, interval)

        # Insert date data into dataframe
        date = result.index
        date = [day.strftime("%H:%M:%S(UTC) - %d/%m/%Y") for day in date[0::].tolist()]
        idx = [x for x in range(1, len(result['Close']) + 1)]
        result.insert(loc=0, column='Index', value=idx)
        result.insert(loc=0, column='Date', value=date)

        # Delete not used columns
        # result = deleteColumns(result, ['Dividends', 'Stock Splits', 'Capital Gains'])
        return result
    
    def getHolders(self): 
        # Get the information of the amount finance product the holders kept
        InstitutionalHolders = self.main.institutional_holders
        MajorHolders = self.main.major_holders
        MutualFundHolders = self.main.mutualfund_holders
        return (InstitutionalHolders, MajorHolders, MutualFundHolders)