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
    def MovingAverage(self, Data, interval): 
        """
        Adding the Moving Average into the dataframe

        Parameters
        ----------
        Data : (pandas DataFrame)
            The DataFrame containing the closing prices.
        interval : (int)
            The number of periods to use for the moving average.
        
        Returns
        -------
        Data : (pandas DataFrame)
            The DataFrame with the Moving Average added.
        """

        # Calculate the moving average
        moving_average = Data['Close'].rolling(interval).mean()

        # Add to the dataset
        Data['Moving Average'] = moving_average
        return Data

    def BollingerBands(self, Data, interval, num_stds = 2):
        """
        Adding the Bollinger Bands into the dataframe
        
        Parameters
        ----------
        Data : (pandas DataFrame)
            The DataFrame containing the closing prices.
        interval : int
            The number of periods to use for the moving average.
        num_stds : float
            The number of standard deviations to use for the bands.
        
        Returns
        -------
        Data : (pandas DataFrame)
            The DataFrame with the Bollinger Bands added.
        """

        # Calculate the moving average
        moving_average = Data['Close'].rolling(interval).mean()
        
        # Calculate the standard deviation
        standard_deviation = Data['Close'].rolling(interval).std()
        
        # Calculate the upper and lower bands
        upper_band = moving_average + num_stds * standard_deviation
        lower_band = moving_average - num_stds * standard_deviation
        
        # Add the bands to the DataFrame
        Data['Bollinger Bands Upper'] = upper_band
        Data['Bollinger Bands Lower'] = lower_band
        return Data