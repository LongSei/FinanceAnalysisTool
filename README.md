# Finance Analysis Tools

![Commits](https://badgen.net/github/commits/LongSei/CryptoAnalysisTool)
![Issues](https://badgen.net/github/issues/LongSei/CryptoAnalysisTool)

## Description
The tool created for basic financial analysis. 

This project is implemented base on these library: 
- yfinance (https://github.com/ranaroussi/yfinance)
- vnquant (https://github.com/phamdinhkhanh/vnquant)
- talib (https://github.com/TA-Lib/ta-lib-python)
- ...

## Installation
```bash
git clone https://github.com/LongSei/FinanceAnalysisTool
```

```bash
pip3 install -r requirements.txt
```

## Features
- Crawling data
- Technical Analysis
- Plot the graph

<!-- #### On-chain Analysis
- Tracking crypto wallets (Updating...) -->

## Usage
:star: You can read the code comment to know exactly which is the input and output of functions

#### Crawling Data
:thought_balloon: import library first
``` python
from crawling.price import * 
```
![plot](./img/crawlingData.png)
:thought_balloon: Return the pandas DataFrame which contains information about your Cryptocurrency
``` python
data = DataCrypto('btc-usd').getHistoricalData(beginTime='01-01-2023', endTime='01-01-2023', interval='1d')
print(data)
```

:thought_balloon: Return pandas DataFrame which contains information about your Vietname Stock Market
``` python
data = DataStock('FPT').getHistoricalData(beginTime='01-01-2023', endTime='01-01-2023')
print(data)
```

``` python
data = DataStock('FPT').getBasicIndex(beginTime='01-01-2023', endTime='01-01-2023')
print(data)
```

#### Add indicator
:thought_balloon: import library first
``` python
from crawling.price import *
```

![plot](./img/addAttribute.png)
:thought_balloon: You need to add the data of your indicator before you can draw it
``` python
data = AddAttribute().SMA(priceData=data, timePeriod=20, priceName='Close', columnName='SMA20')
print(data)
```

#### Plot the graph
:thought_balloon: import library first
``` python
from utils.plot import * 
```
![plot](./img/graphPlotting.png)
:thought_balloon: Add attribute for the graph before draw
```python
# Add attribute
plot.add_attribute(function=plot.candle_stick, row=1, name='Candle Chart')
plot.add_attribute(function=plot.SMA, row=1, name="SMA20")

# Draw the graph
plot.plotGraph(priceData=data)
```

##### Graph List
```
candle_stick         Candle Stick
```

##### Indicator List
```
SMA                  Simple Moving Average
RSI                  Relative Strength Index
BBANDS               Bollinger Bands      
```