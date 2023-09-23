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
git clone https://github.com/LongSei/CryptoAnalysisTool
```

```bash
pip3 install -r requirement.txt
```

## Features
- Crawling data (yfinance)

<!-- #### On-chain Analysis
- Tracking crypto wallets (Updating...) -->

## Usage
:star: You can read the code comment to know exactly which is the input and output of functions

#### Crawling Data
:thought_balloon: Return the pandas DataFrame which contains information about your Cryptocurrency
``` python
# Example with Bitcoin price in a year
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