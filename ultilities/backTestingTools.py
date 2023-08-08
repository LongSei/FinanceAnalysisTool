import numpy as np
import pandas as pd
from crawling.price import * 
import datetime
import time

class Backtesting(): 
    def FilteringData(self, Data, beginTime, endTime): 
        '''
        Filtering the original Data to the suitable period

        Parameters
        ----------
        Data (pandas DataFrame): the original data
        beginTime (String: d/m/Y): Time to buy the finance products 
        endTime (String: d/m/Y): Time to sell the finance products 

        Returns
        -------
        Data (pandas DataFrame): the filtered Data
        '''
        beginTime = time.mktime(datetime.datetime.strptime(beginTime, "%d/%m/%Y").timetuple())
        endTime = time.mktime(datetime.datetime.strptime(endTime, "%d/%m/%Y").timetuple())
        beginIndex = Data[Data['Date'] == datetime.datetime.fromtimestamp(beginTime).strftime("%H:%M:%S(UTC) - %d/%m/%Y")]['Index']
        endIndex = Data[Data['Date'] == datetime.datetime.fromtimestamp(endTime).strftime("%H:%M:%S(UTC) - %d/%m/%Y")]['Index']
        Data = Data[beginIndex.tolist()[0]:(endIndex.tolist()[0] + 1)]
        return Data

    def SingleBuyWithPeriod(self, beginTime, endTime, budget, *financeProduct):
        '''
        BackTesting with the single buy finance product

        Parameters
        ----------
        beginTime (String: d/m/Y): Time to buy the finance products 
        endTime (String: d/m/Y): Time to sell the finance products 
        financeProduct (String): the id of product want to buy (ex: btc-usd, eth-usd, aapl-usd,...)
        budget: the amount money want to buy

        Returns 
        -------
        Result Format: [{"Product": financeProduct, "Return": [Max Price, Min Price, Total LossOrGain, Status]},...]
            Max Price (Int): the max price the product reach in the period
            Min Price (Int): the min price the product reach in the period
            Total LossOrGain (Int): the money we make or loss after the period
            Status (String): the status of the backtesting (Loss Money or Make Profit)
        ''' 
        result = list()
        for product in financeProduct:
            Data = DataGetting(product).getHistoricalData(period='max', interval='1d')
            Data = self.FilteringData(Data, beginTime, endTime)

            # BackTesting
            maxPrice = Data["Close"].max()
            minPrice = Data["Close"].min()
            profit = (Data["Close"][-1] - Data["Close"][0]) * (budget / Data["Close"][0])
            status = "Make Profit" if profit > 0 else "Lose Money"
            
            print(f"Summary Investment Period: {Data['Date'][0]} to {Data['Date'][-1]}")
            print("Max Price: ", maxPrice)
            print("Min Price: ", minPrice)
            print("Total Gain: " if status == "Make Profit" else "Total Loss: ", abs(profit))
            print("Status: ", status)
            result.append({"Product": product, "Return": [maxPrice, minPrice, profit, status]})
        return result
    
    def MultipleBuyWithInterval(self, beginTime, endTime, amountPerBuy, interval, *financeProduct): 
        '''
        BackTesting with the multiple buy for an fixed interval time

        Parameters
        ----------
        beginTime (String: d/m/Y): Time to buy the finance products 
        endTime (String: d/m/Y): Time to sell the finance products 
        amountPerBuy (Function): calculate amount money want to buy in each time
            Parameters: DayConsidered, PriceData
            Returns: amount money spent for that buy order
        interval (Int): interval between each buy order
        financeProduct (String): the id of product want to buy (ex: btc-usd, eth-usd, aapl-usd,...)

        Returns
        -------
        Result Format: [{"Product": financeProduct, "Return": [Max Price, Min Price, Total Spend, Total LossOrGain, Status]},...]
            Max Price (Int): the max price the product reach in the period
            Min Price (Int): the min price the product reach in the period
            Total Spend (Int): the money spent
            Total LossOrGain (Int): the money we make or loss after the period
            Status (String): the status of the backtesting (Loss Money or Make Profit)
        '''

        result = list()
        for product in financeProduct:
            Data = DataGetting(product).getHistoricalData(period='max', interval='1d')
            Data = self.FilteringData(Data, beginTime, endTime)
            totalSpend = 0
            totalBought = 0
            totalDay = len(Data['Close'].tolist())
            for day in range(0, totalDay, interval): 
                totalSpend += amountPerBuy(day, Data)
                totalBought += amountPerBuy(day, Data) / Data['Close'][day]
    
            maxPrice = Data["Close"].max()
            minPrice = Data["Close"].min()
            profit = Data['Close'][-1] * totalBought - totalSpend
            status = "Make Profit" if profit > 0 else "Lose Money"

            print(f"Summary Investment Period: {Data['Date'][0]} to {Data['Date'][-1]}")
            print("Max Price: ", maxPrice)
            print("Min Price: ", minPrice)
            print("Total Spend: ", totalSpend)
            print("Total Gain: " if status == "Make Profit" else "Total Loss: ", abs(profit))
            print("Status: ", status)
            result.append({"Product": product, "Return": {"Max Price": maxPrice, "Min Price": minPrice, "Total Spend": totalSpend, "Total Gain": profit, "Status": status}})
        return result
    
    def MultipleBuyWithCondition(self, beginTime, endTime, condition, *financeProduct):
        '''
        BackTesting with a condition for each buying time

        Parameters
        ----------
        beginTime (String: d/m/Y): Time to buy the finance products 
        endTime (String: d/m/Y): Time to sell the finance products 
        condition (Function): decision when to place the order and amount of money spending for that order
           Parameters: DayConsidered, PriceData
           Returns: Positive/Buy || Zero/DoNothing || Negative/Sell
        financeProduct (String): the id of product want to buy (ex: btc-usd, eth-usd, aapl-usd,...)

        Returns
        -------
        Result Format: [{"Product": financeProduct, "Return": [Max Price, Min Price, Total Spend, Total LossOrGain, Status]},...]
            Max Price (Int): the max price the product reach in the period
            Min Price (Int): the min price the product reach in the period
            Total Spend (Int): the money spent
            Total LossOrGain (Int): the money we make or loss after the period
            Status (String): the status of the backtesting (Loss Money or Make Profit)
        '''

        result = list()
        for product in financeProduct: 
            Data = DataGetting(product).getHistoricalData(period='max', interval='1d')
            Data = self.FilteringData(Data, beginTime, endTime)
            totalDay = len(Data['Close'].tolist())
            amountMoney = 0
            totalSpend = 0
            totalBought = 0

            for day in range(0, totalDay): 
                decision = condition(day, Data)
                if decision > 0:
                    totalSpend += decision
                    amountMoney -= decision
                    totalBought += decision / Data['Close'][day]
                elif decision < 0: 
                    amountMoney += decision
                    totalBought -= decision / Data['Close'][day]

            amountMoney += totalBought * Data['Close'][-1]

            maxPrice = Data["Close"].max()
            minPrice = Data["Close"].min()
            profit = amountMoney 
            status = "Make Profit" if profit > 0 else "Lose Money"

            print(f"Summary Investment Period: {Data['Date'][0]} to {Data['Date'][-1]}")
            print("Max Price: ", maxPrice)
            print("Min Price: ", minPrice)
            print("Total Spend: ", totalSpend)
            print("Total Gain: " if status == "Make Profit" else "Total Loss: ", abs(profit))
            print("Status: ", status)
            result.append({"Product": product, "Return": {"Max Price": maxPrice, "Min Price": minPrice, "Total Spend": totalSpend, "Total Gain": profit, "Status": status}})
        return result