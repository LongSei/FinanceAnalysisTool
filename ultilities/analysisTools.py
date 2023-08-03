import matplotlib.pyplot as plt
import numpy as np
class MomentumAnalysis(): 
    def priceCorrelation(self, priceDict: list):
        """
        Plot the correlation between coins

        Parameters
        ----------
        priceDict (list of dictionary):
            Name (String): the id of coin: (ex: BTC, ETH,...)
            Data (list): the data contain price of coin
        """
        amountCoin = len(priceDict)
        def dividePlot(amountGraph): 
            rowAndCol = [1, amountGraph]
            for i in range(1, int(amountGraph ** 0.5) + 1): 
                if (amountGraph % i) == 0: 
                    rowAndCol = [i, int(amountGraph / i)]
            return rowAndCol
        
        [row, col] = dividePlot(amountCoin)
        if (row < col): 
            row, col = col, row
        fig, axs = plt.subplots(row, col)
        for r in range(0, row): 
            for c in range(0, col): 
                idxOfCoin = col * r + c
                if row != 1 and col != 1:
                    axs[r, c].set_title(priceDict[idxOfCoin]['Name'])
                    axs[r, c].plot(priceDict[idxOfCoin]['Data'])
                else: 
                    axs[r].set_title(priceDict[idxOfCoin]['Name'])
                    axs[r].plot(priceDict[idxOfCoin]['Data'])
        fig.tight_layout()
        plt.show()

class Indicators(): 
    def IncreaseOrDecrease(self, Data): 
        """
        Adding the Status for each day. Whether it increase or decrease with the previous day

        Parameters
        ----------
        Data : (pandas DataFrame)
            The data consist of closing prices
        
        Returns
        -------
        Data : (pandas DataFrame)
            The DataFrame with Status of price
        """

        if ('Status' in Data.columns) == True: 
            return Data
        
        StatusPrice = ["Increase"]
        for i in range(1, len(Data['Close'])): 
            if (Data['Close'][i - 1] > Data['Close'][i]): 
                StatusPrice.append("Decrease")
            else: 
                StatusPrice.append("Increase")

        Data['Status'] = StatusPrice
        return Data
    
    def RelativeStrengthIndex(self, Data, interval): 
        """
        Adding the Relative Strength Index into the dataframe

        Parameters
        ----------
        Data : (pandas DataFrame)
            The data consist of close prices and status of prices. 
        interval: (int)
            The interval used for the rsi 

        Returns
        -------
        Data : (pandas DataFrame)
            The DataFrame with the RSI added
        """
        
        Data = self.IncreaseOrDecrease(Data)
        closePrice = Data['Close']
        statePrice = Data['Status']
        
        rsi = [0 for x in range(interval - 1)]

        # Calculate the first RSI
        avgGain = 0
        avgLoss = 0
        for day in range(0, interval): 
            if (Data['Status'][day] == "Increase"): 
                avgGain += Data['Close'][day] / interval
            else: 
                avgLoss += Data['Close'][day] / interval
        rs = avgGain / avgLoss
        rsi.append(100 - (100 / (1 + rs)))

        # Calculate other RSI
        for day in range(interval, len(Data['Close'])): 
            changePrice = abs(Data['Close'][day - 1] - Data['Close'][day])
            if (Data['Status'][day] == "Increase"): 
                avgGain = (avgGain * (interval - 1) + changePrice) / interval
                avgLoss = (avgLoss * (interval - 1)) / interval
            else: 
                avgGain = (avgGain * (interval - 1)) / interval
                avgLoss = (avgLoss * (interval - 1) + changePrice) / interval
            if (avgLoss == 0): 
                rsi.append(100)
            else: 
                rs = avgGain / avgLoss
                rsi.append(100 - (100 / (1 + rs)))
                
        Data["Relative Strength Index"] = rsi
        return Data

    def MovingAverage(self, Data, interval): 
        """
        Adding the Moving Average into the dataframe

        Parameters
        ----------
        Data : (pandas DataFrame)
            The data consist of close prices.
        interval : (int)
            The interval used for the moving average.
        
        Returns
        -------
        Data : (pandas DataFrame)
            The DataFrame with the Moving Average added.
        """

        moving_average = Data['Close'].rolling(interval).mean()

        Data['Moving Average'] = moving_average
        return Data

    def BollingerBands(self, Data, interval, num_stds = 2):
        """
        Adding the Bollinger Bands into the dataframe
        
        Parameters
        ----------
        Data : (pandas DataFrame)
            The data consist of close prices.
        interval : int
            The interval used for the moving average.
        num_stds : float
            The number of standard deviations to use for the bands.
        
        Returns
        -------
        Data : (pandas DataFrame)
            The DataFrame with the Bollinger Bands added.
        """

        moving_average = Data['Close'].rolling(interval).mean()
        
        standard_deviation = Data['Close'].rolling(interval).std()
        
        upper_band = moving_average + num_stds * standard_deviation
        lower_band = moving_average - num_stds * standard_deviation
        
        Data['Bollinger Bands Upper'] = upper_band
        Data['Bollinger Bands Lower'] = lower_band
        return Data