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
- Crawling data (yfinance)
- BackTesting
- Technical Indicators
- Tracking crypto wallet

## Tools 
#### BackTesting
- Single order
- Multiple order (fixed interval, with condition,...)

#### Momentum Analysis
- Correlation Graph
- Updating...

#### Indicators Analysis
- SMA - Moving Average
- RSI - Relative Strength Index 
- BB - Bollinger Bands
- Updating...
<!-- Future feature -->
<!-- #### On-chain Analysis -->
<!-- #### News Analysis -->

#### On-chain Analysis
- Tracking crypto wallets (Updating...)

## Usage
:star: You can read the code comment to know exactly which is the input and output of functions

#### BackTesting
:thought_balloon: Return the result for backtesting
``` python
# Example with Single order
beginTime = "12/02/2023"
endTime = "12/03/2023"
budget = 1000
result = BackTesting().SingleBuyWithPeriod(beginTime, endTime, budget, 'btc-usd')
print(result)
```

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
