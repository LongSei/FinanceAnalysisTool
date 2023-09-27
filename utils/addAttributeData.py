import talib
class AddAttribute(): 
    class TechnicalAnalysis():
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
