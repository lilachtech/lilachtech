import pandas as pd
import os

fileNames = ['1Q.csv', '2Q.csv', '3Q.csv', '4Q.csv', '5Q.csv', '6Q.csv', '7Q.csv', 'ques_rows_export_2.csv']
dfList = []

for f in fileNames:
    df = pd.read_csv(f, header=None, error_bad_lines=False)
    dfList.append(df)
    print(df)

concatDf = pd.concat(dfList, axis=0)
concatDf.to_csv('Combine_q.csv', index=None)
