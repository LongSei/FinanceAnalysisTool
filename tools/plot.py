import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from crawling.price import * 
from crawling.wallet import * 

class PlotData(): 
    def __init__(self, namePlot) -> None:
        self.figRows = 1
        self.figCols = 1
        self.fig = make_subplots(rows = self.figRows, cols = self.figCols)
        self.fig_attributes = {'attributes': [],
                               'plots': [{'name': namePlot, 'index': 1}]}
        self.fig.update_xaxes(rangeslider_thickness = 0.1)
        self.fig.update_yaxes(fixedrange=False)
        # fig_attributes: {'attributes', 'plots'}
        # attributes: [{'function', 'row', 'name'}]
        # plots: [{'name', 'index'}]

    def add_attribute(self, function, row, name): 
        '''
        Usage
        -----
        Add the attribute for the graph

        Parameters
        ----------
        function (function): the function you want to plot on the figure
        row (int): the graphIndex to plot 
        name (str): name of the attribute
        '''
        newAttribute = dict()
        newAttribute['function'] = function
        newAttribute['row'] = row
        newAttribute['name'] = name
        self.fig_attributes['attributes'].append(newAttribute)

    def add_plot(self, name): 
        '''
        Usage
        -----
        Add the graph for the figure

        Parameters
        ----------
        name (str): name of the graph
        '''
        index = len(self.fig_attributes['plots'])
        newPlot = dict()
        newPlot['index'] = index + 1
        newPlot['name'] = name
        self.fig_attributes['plots'].append(newPlot)

    def update_row_and_col(self, rows, cols): 
        self.figRows = rows
        self.figCols = cols
        titles = [plot['name'] for plot in self.fig_attributes['plots']]
        self.fig = make_subplots(rows = self.figRows, cols = self.figCols, subplot_titles=titles, shared_xaxes=True, vertical_spacing=0.1)
        self.fig.update_xaxes(rangeslider_thickness=0.05, row=1,col=1)
        self.fig.update_yaxes(fixedrange=False)

    def plotGraph(self, priceData): 
        '''
        Usage 
        -----
        Plotting the graph 

        Parameters
        ----------
        priceData (DataFrame): the data you want to draw base on
        '''
        amountRow = 0
        listRows = [attribute['row'] for attribute in self.fig_attributes['attributes']]
        attemp = reMaskValue(listRows)
        listRows = attemp['newList']
        for idx in range(0, len(self.fig_attributes['attributes'])): 
            self.fig_attributes['attributes'][idx]['row'] = listRows[idx] + 1
        amountRow = attemp['amountMask']
        
        amountCol = len(self.fig_attributes['plots'])
        if (amountRow != self.figRows or amountCol != self.figCols):
            self.update_row_and_col(rows=amountRow, cols=amountCol) 

        for plot in self.fig_attributes['plots']: 
            for attribute in self.fig_attributes['attributes']: 
                attribute['function'](attribute['row'], plot['index'], attribute['name'], priceData)

        self.fig.show()

    def candle_stick(self, plotRow, plotCol, name, priceData): 
        '''
        Usage
        -----
        Add candle stick on the graph

        Parameters
        ----------
        plotRow, plotCol (int): coordinate of the attribute
        name (str): name of the attribute
        priceData (DataFrame): the data you want to draw base on
        '''
        dateVariable = priceData['Date']
        openVariable = priceData['Open']
        closeVariable = priceData['Close']
        highVariable = priceData['High']
        lowVariable = priceData['Low']

        self.fig.append_trace(go.Candlestick(x=dateVariable,
                                          open=openVariable,
                                          close=closeVariable, 
                                          high=highVariable, 
                                          low=lowVariable, 
                                          name=name),
                            row=plotRow, col=plotCol, 
                            )
        
    def Volume(self, plotRow, plotCol, name, priceData): 
        '''
        Usage
        -----
        Add candle stick on the graph

        Parameters
        ----------
        plotRow, plotCol (int): coordinate of the attribute
        name (str): name of the attribute
        priceData (DataFrame): the data you want to draw base on
        '''
        dateVariable = priceData['Date']
        volumeVariable = priceData[name]
        self.fig.append_trace(go.Bar(x=dateVariable, 
                                     y=volumeVariable, 
                                     name=name), 
                            row = plotRow, 
                            col = plotCol)
        
    def SMA(self, plotRow, plotCol, name, priceData):
        '''
        Usage
        -----
        Add candle stick on the graph

        Parameters
        ----------
        plotRow, plotCol (int): coordinate of the attribute
        name (str): name of the attribute
        priceData (DataFrame): the data you want to draw base on
        '''
        dateVariable = priceData['Date']
        macdVariable = priceData[name]
        self.fig.append_trace(go.Scatter(x=dateVariable, y=macdVariable, name=name), 
                           row=plotRow, col=plotCol)
        
    def RSI(self, plotRow, plotCol, name, priceData): 
        '''
        Usage
        -----
        Add candle stick on the graph

        Parameters
        ----------
        plotRow, plotCol (int): coordinate of the attribute
        name (str): name of the attribute
        priceData (DataFrame): the data you want to draw base on
        '''
        dateVariable = priceData['Date']
        rsiVariable = priceData[name]

        self.fig.append_trace(go.Scatter(x=dateVariable, y=rsiVariable, name=name), 
                           row=plotRow, col=plotCol)
        
        self.fig.add_hline(y=70, line_dash="dot", row=plotRow, col=plotCol,
                  annotation_text="70%", 
                  annotation_position="bottom right")

        self.fig.add_hline(y=30, line_dash="dot", row=plotRow, col=plotCol,
                  annotation_text="30%", 
                  annotation_position="bottom right")
        
    def BBANDS(self, plotRow, plotCol, name, priceData):
        '''
        Usage
        -----
        Add candle stick on the graph

        Parameters
        ----------
        plotRow, plotCol (int): coordinate of the attribute
        name (str): name of the attribute
        priceData (DataFrame): the data you want to draw base on
        '''
        dateVariable = priceData['Date']
        values = priceData[name].copy().tolist()
        UpperVariable = [value[0] for value in values]
        MiddleVariable = [value[1] for value in values]
        LowerVariable = [value[2] for value in values]

        self.fig.append_trace(
                            go.Scatter(x=dateVariable, y=UpperVariable, name=name + " - Upper"),
                            row=plotRow, col=plotCol)
        
        self.fig.append_trace(
                            go.Scatter(x=dateVariable, y=MiddleVariable, name=name + " - Middle"),
                            row=plotRow, col=plotCol)
        
        self.fig.append_trace(
                            go.Scatter(x=dateVariable, y=LowerVariable, name=name + " - Lower"),
                            row=plotRow, col=plotCol)