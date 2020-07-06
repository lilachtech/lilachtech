import pandas as pd
import os

fileNames = ['data0.csv', 'data1.csv', 'data2.csv', 'data3.csv', 'data4.csv', 'data5.csv', 'data6.csv', 'data7.csv',
             'data8.csv', 'data9.csv', 'data10.csv', 'data11.csv', 'data12.csv', 'data13.csv', 'data14.csv',
             'data14.csv', 'data15.csv', 'data16.csv', 'data17.csv', 'data18.csv', 'data19.csv']

dfList = []

for f in fileNames:
    dfList.append(Dataframes)

concatDf = pd.concat(dfList, axis=0)
concatDf.columns = DataHeaders
concatDf.to_csv('Combine.csv', index=None)
