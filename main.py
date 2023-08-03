from ultilities.databaseTools import * 
from crawling.wallet import * 
from crawling.price import *
from ultilities.analysisTools import *

class Testing():
    def CorrelationTest(self):
        btcData = DataGetting('btc-usd').getHistoricalData('1y')
        ethData = DataGetting('eth-usd').getHistoricalData('1y')
        dogeData = DataGetting('doge-usd').getHistoricalData('1y')
        btcPrice = btcData['Close'].copy().tolist()
        ethPrice = ethData['Close'].copy().tolist()
        dogePrice = dogeData['Close'].copy().tolist()

        MomentumAnalysis().priceCorrelation([{'Name': 'BTC', 'Data': btcPrice}, 
                                            {'Name': 'ETH', 'Data': ethPrice}, 
                                            {'Name': 'Doge', 'Data': dogePrice}])
    
    def RsiTest(self): 
        btcData = DataGetting('btc-usd').getHistoricalData('1y')
        btcData = Indicators().RelativeStrengthIndex(Data=btcData, interval=14)
        print(btcData['Relative Strength Index'])
        plt.plot(btcData['Relative Strength Index'])
        plt.show()

Testing().RsiTest()
# Testing().CorrelationTest()