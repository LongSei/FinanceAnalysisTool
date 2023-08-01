from ultilities.databaseTools import * 
from crawling.wallet import * 
from crawling.price import *
from ultilities.analysisTools import *

class Testing():
    def CorrelationTest(self):
        btcData = DataGetting('btc-usd').getHistoricalData()
        ethData = DataGetting('eth-usd').getHistoricalData()
        dogeData = DataGetting('doge-usd').getHistoricalData()
        btcPrice = btcData['Close'].copy().tolist()
        ethPrice = ethData['Close'].copy().tolist()
        dogePrice = dogeData['Close'].copy().tolist()

        MomentumAnalysis().priceCorrelation([{'Name': 'BTC', 'Data': btcPrice}, 
                                            {'Name': 'ETH', 'Data': ethPrice}, 
                                            {'Name': 'Doge', 'Data': dogePrice}])

Testing().CorrelationTest()