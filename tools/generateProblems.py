from tools.plot import * 
import random
from utils.function import randomDateRange
import sys, os
import datetime
class generateProblems(): 
    def __init__(self, tickers: list) -> None:
        self.tickers = tickers 
        self.dataProblem = pd.DataFrame
        self.dataResult = pd.DataFrame
    
    def generateStock(self, problemLen, resultLen): 
        self.generate(problemLen, resultLen, 'stock')
    def generateCrypto(self, problemLen, resultLen): 
        self.generate(problemLen, resultLen, 'crypto')

    def generate(self, problemLen, resultLen, typeFinanceProduct): 
        lenResult = problemLen + resultLen
        if (lenResult < 20):
            exit("'lenResult' must be more than or equal 20") 

        print("Data Generating..........")
        try: 
            self.createData(problemLen, resultLen, typeFinanceProduct.lower())
        except: 
            exit("Cannot generate new problem !!!")

        if not os.path.exists('./ProblemSet'):
            os.makedirs('./ProblemSet')
            
        print("Data have been generated !")
        print("You can see the problem data in 'ProblemSet' folder")
        self.dataProblem.to_csv('ProblemSet/ProblemData.csv')
        self.dataResult.to_csv('ProblemSet/ResultData.csv')

    def createData(self, problemLen, resultLen, typeFinanceProduct): 
        beginTime = '2017-01-01'
        endTime = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        lenResult = problemLen + resultLen

        ticker = random.choice(self.tickers)
        if typeFinanceProduct == 'stock': 
            data = DataStock(ticker).getHistoricalData(beginTime=beginTime, endTime=endTime)
        elif typeFinanceProduct == 'crypto': 
            data = DataCrypto(ticker).getHistoricalData(beginTime=beginTime, endTime=endTime)
        else: 
            exit("'typeFinanceProduct' must be 'stock' or 'crypto'")
        beginIdx = random.randint(0, len(data) - lenResult)
        endIdx = beginIdx + lenResult - 1
        data = data.loc[beginIdx:endIdx]
        data = data.reset_index(drop=True)
        self.dataProblem = data.loc[0:(problemLen - 1)]
        self.dataResult = data.loc[(problemLen):(lenResult)]
    
    def show(self): 
        plot = PlotData('Problem')
        plot.add_attribute(plot.candle_stick, 1, 'Candle Chart')
        plot.plotGraph(self.data)

