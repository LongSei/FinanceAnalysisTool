from ultilities.databaseTools import * 
from crawling.wallet import * 
from crawling.price import *
from ultilities.analysisTools import *
from ultilities.machineLearningTools import *

class Testing():
    def CorrelationTest(self):
        btcData = DataGetting('btc-usd').getHistoricalData('1y')
        ethData = DataGetting('eth-usd').getHistoricalData('1y')
        btcPrice = btcData['Close'].copy().tolist()
        ethPrice = ethData['Close'].copy().tolist()

        Momentum().Correlation([{'Name': 'BTC', 'Data': btcPrice}, 
                                            {'Name': 'ETH', 'Data': ethPrice}
                                            ])
    
    def RsiTest(self): 
        btcData = DataGetting('btc-usd').getHistoricalData('1y')
        btcData = Indicator().RelativeStrengthIndex(Data=btcData, interval=14)
        print(btcData['Relative Strength Index'])
        plt.plot(btcData['Relative Strength Index'])
        plt.show()

    def machineLearning(self): 
        btcData = DataGetting('btc-usd').getHistoricalData('4y')
        model = MachineLearning().LSTM(btcData, 30)
        model.runLSTM()
        plt.plot(model.modelPredict(model.xTest))
        plt.plot(model.yTest)
        plt.show()

# Testing().machineLearning()