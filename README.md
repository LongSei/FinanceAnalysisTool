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
- Crawling crypto data
- Technical Indicators

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
<!-- #### Machine Learning Analysis  -->
<!-- #### On-chain Analysis -->
<!-- #### News Analysis -->

## Usage
:star: You can read the code comment to know exacly which is the input and output of functions
#### Crawling Data
:thought_balloon: Return the pandas DataFrame which contains information about the finance products
``` python
# Example with Bitcoin price in a year
btcData = DataGetting('btc-usd').getHistoricalData(period='1y', interval='1d')
print(btcData)
```
#### Momentum Analysis
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