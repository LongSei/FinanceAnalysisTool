from tools.plot import * 
import random
from utils.function import randomDateRange
import sys, os
import datetime
import pandas as pd
class generateProblems(): 
    def __init__(self) -> None:
        self.tickers = list
        self.dataProblem = pd.DataFrame
        self.dataResult = pd.DataFrame

    def solve(self, id): 
        try: 
            problemData = pd.read_csv('./ProblemSet/Problem_' + str(id) + "/ProblemData.csv")
            resultData = pd.read_csv('./ProblemSet/Problem_' + str(id) + "/ResultData.csv")
        except: 
            exit("\x1b[1;31mCannot open Problem_" + str(id) + "\x1b[0m")

        priceResult = resultData.iloc[-1]['Close']
        priceInput = problemData.iloc[-1]['Close']
        sys.stdout.write("\x1b[1;35mChoose your order: \n\x1b[0m")
        sys.stdout.write("1) \x1b[1;32mBuy \n\x1b[0m")
        sys.stdout.write("2) \x1b[1;31mSell \n\x1b[0m")

        order = int(input("\x1b[1mType your order (1 | 2): \x1b[0m"))

        profit = int
        if (order == 1): 
            profit = ((priceResult / priceInput) - 1) * 100
            profit = int(round(profit, 2))
        elif (order == 2): 
            profit = (1 - (priceResult / priceInput)) * 100
            profit = int(round(profit, 2))
        else: 
            exit("\x1b[1;31mYou must type '1' or '2'\x1b[0m")
        profitOrLoss = True if profit >= 0 else False
        if profitOrLoss == True: 
            returnCommand = "\x1b[1;32mCongratulation !!! Your profit is: " + str(profit) + "%\x1b[0m"
        else: 
            returnCommand = "\x1b[1;31mSorry ! But you lost: " + str(profit) + "%\x1b[0m"
        sys.stdout.write(returnCommand)

        order = str(input("\x1b[1mDo you want to delete this problem ? (YES | NO): \x1b[0m")).lower()
        if (order[0] == 'y'): 
            try:
                self.__deleteData(id)
                sys.stdout.write("\x1b[1;32mProblem_" + str(id) + " deleted\x1b[0m")
            except: 
                sys.stdout.write("\x1b[1;31mCannot delete Problem_" + str(id) + "\x1b[0m")
        else: 
            sys.stdout.write("\x1b[1;35mProblem_" + str(id) + " still be there\x1b[0m")

    def generate(self, tickers, problemLen, resultLen, typeFinanceProduct): 
        '''
        Usage
        -----
        Use to create interact with user

        Parameters
        ----------
        tickers (list): a list of finance product to create problem
        problemLen (int): Size of problem_data generated
        resultLen (int): Size of result_data generated
        typeFinanceProduct (str): type of data generated ('crypto' || 'stock')
        '''

        lenResult = problemLen + resultLen
        if (lenResult < 20):
            exit("\x1b[1;31m'lenResult' must be more than or equal 20\x1b[1;0m") 

        try: 
            isGenerated = False
            self.tickers = tickers
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if isGenerated:
                        break
                    sys.stdout.write('\r\x1b[1mData Generating \x1b[0m' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
            thread = threading.Thread(target=animate)
            thread.start()
            self.__createData(problemLen, resultLen, typeFinanceProduct.lower())
            sys.stdout.write('\n')

            if not os.path.exists('./ProblemSet'):
                os.makedirs('./ProblemSet')
            problemPath = os.getcwd() + '/ProblemSet'
            listProblem = os.listdir(os.getcwd() + '/ProblemSet')
            problemId = str(random.randint(1, 99999)) 
            while len(problemId) < 5: 
                problemId = '0' + problemId
            while ("Problem_" + problemId) in listProblem:
                problemId = str(random.randint(1, 99999)) 
                while len(problemId) < 5: 
                    problemId = '0' + problemId

            if not os.path.exists('./ProblemSet/Problem_' + problemId):
                os.makedirs('./ProblemSet/Problem_' + problemId)
            problemPath = './ProblemSet/Problem_' + problemId
            self.dataProblem.to_csv(problemPath + '/ProblemData.csv', index=False)
            self.dataResult.to_csv(problemPath + '/ResultData.csv', index=False)

            isGenerated = True
            sys.stdout.write("\x1b[1;32mData have been generated !\x1b[1;0m" + '\n')
            sys.stdout.write("\x1b[1;35mYou can see the problem data in '" + problemPath + "' folder\x1b[1;0m" + '\n')
            sys.stdout.write("\x1b[1;35mYou can submit answer for the problem by running this: \x1b[1;0m 'python main.py --submit [problemId]'" + '\n')
        except: 
            isGenerated = True
            sys.stdout.write('\n')
            exit("\x1b[1;31mCannot generate new problem !!!\x1b[1;0m")


    def __createData(self, problemLen, resultLen, typeFinanceProduct): 
        '''
        Usage
        -----
        Use to create data

        Parameters
        ----------
        problemLen (int): Size of problem_data generated
        resultLen (int): Size of result_data generated
        typeFinanceProduct (str): type of data generated ('crypto' || 'stock')
        '''

        beginTime = '2017-01-01'
        endTime = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        lenResult = problemLen + resultLen

        ticker = random.choice(self.tickers)
        if typeFinanceProduct == 'stock': 
            data = DataStock(ticker).getHistoricalData(beginTime=beginTime, endTime=endTime)
        elif typeFinanceProduct == 'crypto': 
            data = DataCrypto(ticker).getHistoricalData(beginTime=beginTime, endTime=endTime)
        else: 
            exit("\x1b[1;31m'typeFinanceProduct' must be 'stock' or 'crypto'\x1b[1;0m")
        beginIdx = random.randint(0, len(data) - lenResult)
        endIdx = beginIdx + lenResult - 1
        data = data.loc[beginIdx:endIdx]
        data = data.reset_index(drop=True)
        self.dataProblem = data.loc[0:(problemLen - 1)]
        self.dataResult = data.loc[(problemLen):(lenResult)]

    def __deleteData(self, id): 
        path = os.getcwd() + "/ProblemSet/Problem_" + str(id)
        if os.path.exists(path + "/ProblemData.csv"): 
            os.remove(path + "/ProblemData.csv")
        if os.path.exists(path + "/ResultData.csv"): 
            os.remove(path + "/ResultData.csv")
        if os.path.exists(path): 
            os.rmdir(path)