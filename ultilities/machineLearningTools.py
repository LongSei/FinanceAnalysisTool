import pandas as pd
import numpy as np
import csv
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.activations import relu
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense,LSTM, Lambda, Input

class MachineLearning(): 
    class LSTM(): 
        '''
        The LSTM ModelFrame to predicting 

        Parameters
        ----------
        Data : (pandas DataFrame)
            The data consist of close prices.
        lookBackDay: (int)
            The interval the LSTM model lookback
        ratioTesting: (float)
            The ratio used to split the Data

        Returns
        -------
        The machine learning model - LSTM
        * Note: The input for the model should have the same length as the lookBackDay parameters
        '''
        
        def __init__(self, Data, lookBackDay = 30, ratioTesting = 0.1) -> None:
            self.lookBackDay = lookBackDay
            self.Data = Data
            self.ratioTesting = ratioTesting
        
        def dataPrepare(self, rateTesting=0): 
            self.xTrain = []
            self.yTrain = []
            for yDay in range(self.lookBackDay, len(self.Data)):
                self.yTrain.append(self.Data['Close'][yDay])
                self.xTrain.append([self.Data['Close'][x] for x in range(yDay - self.lookBackDay, yDay)])

            testSize = int(len(self.xTrain) * self.ratioTesting)
            self.xTest = self.xTrain[(len(self.xTrain) - testSize):]
            self.yTest = self.yTrain[(len(self.yTrain) - testSize):]
            self.xTrain = self.xTrain[:(len(self.xTrain) - testSize)]
            self.yTrain = self.yTrain[:(len(self.yTrain) - testSize)]

        def modelBuild(self): 
            tf.random.set_seed(42)
            inputs = Input(shape=self.lookBackDay)
            self.model = Lambda(lambda x: tf.expand_dims(x, axis=1))(inputs)
            self.model = LSTM(200, activation='relu', return_sequences=True)(self.model)
            self.model = LSTM(100, activation='relu', return_sequences=True)(self.model)
            self.model = LSTM(50, activation='relu', return_sequences=True)(self.model)
            self.model = LSTM(25, activation='relu')(self.model)
            self.model = Dense(20, activation='relu')(self.model)
            self.model = Dense(10, activation='relu')(self.model)
            output = Dense(1)(self.model)
            self.model = tf.keras.Model(inputs=inputs, outputs=output, name="model_5_LSTM")
            self.model.compile(loss='mae', optimizer=tf.keras.optimizers.legacy.Adam())

        def modelShow(self): 
            print(self.model.summary())

        def modelFit(self): 
            history = self.model.fit(
                        self.xTrain,
                        self.yTrain,
                        epochs=100,
                        verbose=1,
                        batch_size = 32,
                        validation_data=(self.xTest, self.yTest))
        
        def modelPredict(self, DataPredict): 
            result = self.model.predict(DataPredict)
            return result
        
        def runLSTM(self): 
            self.dataPrepare()
            self.modelBuild()
            self.modelFit()
