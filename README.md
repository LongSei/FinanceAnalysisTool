# Cryptocurrency Analysis Tools

![Commits](https://badgen.net/github/commits/LongSei/CryptoAnalysisTool)
![Issues](https://badgen.net/github/issues/LongSei/CryptoAnalysisTool)

## Description
This tool is supported for the most basic analysis of financial products like stocks, crypto,...

## Requirements
```
matplotlib==3.7.1
numpy==1.24.3
pandas==2.0.3
Requests==2.31.0
yfinance==0.2.22
```
## Features
- Crawling data
- Technical Indicators
- Tracking crypto wallet

## Tools 
#### Momentum Analysis
- Correlation Graph
- Updating...

#### Indicators Analysis
- SMA - Moving Average
- RSI - Relative Strength Index 
- BB - Bollinger Bands
- Updating...
<!-- Future feature -->
#### Machine Learning Analysis 
- LSTM 
<!-- #### On-chain Analysis -->
<!-- #### News Analysis -->

#### On-chain Analysis
- Tracking crypto wallets (Updating...)
## Usage
:star: You can read the code comment to know exactly which is the input and output of functions

#### Crawling Data
:thought_balloon: Return the pandas DataFrame which contains information about the finance products
``` python
# Example with Bitcoin price in a year
btcData = DataGetting('btc-usd').getHistoricalData(period='1y', interval='1d')
print(btcData)
```

#### Momentum Analysis
![plot](/img/Momentum/CorrelationTest.png)

:thought_balloon: Consider the price movement of coins
``` python
# Example with correlation between price of finance products
btcData = DataGetting('btc-usd').getHistoricalData('1y').copy().tolist()
ethData = DataGetting('eth-usd').getHistoricalData('1y').copy().tolist()

Momentum().Correlation([{'Name': 'BTC', 'Data': btcPrice}, 
                        {'Name': 'ETH', 'Data': ethPrice}])
```

#### Indicators Analysis
:thought_balloon: Add the data of indicator to the DataFrame which was putting as input for the function
``` python
# Example with SMA
btcData = DataGetting('btc-usd').getHistoricalData('1y').copy().tolist()
btcData = Indicator().MovingAverage(Data=btcData, interval=14)
print(btcData)
```

#### Machine Learning Analysis
##### Training Plot
<img src="/img/Machine%20Learning/LSTM/TrainGraph.png" alt="TrainGraph" width="200"/>

##### Testing Plot
<img src="/img/Machine%20Learning/LSTM/TestGraph.png" alt="TestGraph" width="200"/>

##### Predict Plot
<img src="/img/Machine%20Learning/LSTM/PredictGraph.png" alt="PredictGraph" width="200"/>

:thought_balloon: Applied machine learning to predict the future price of finance products

``` python
# Example with predicting bitcoin price using LSTM
btcData = DataGetting('btc-usd').getHistoricalData('4y')
model = MachineLearning().LSTM(btcData, 30)
model.runLSTM()
print(model.predict(predictData))
```