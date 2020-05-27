import pandas as pd
import os

fileNames = ['5aaa7bde56c51000018cc7b5.csv', '5b2973a08c745200013b84ae.csv', '5e68ff434db49c01d7dbedd2.csv',
             '5e836b26ac330b064f3c861e.csv', '54da5755fdf99b2ae8ab221c.csv', '5806b9d1084b750001dbcde0.csv']

dfList = []
# DataHeaders = ['Date', 'Text']

for f in fileNames:
    Dataframes = pd.read_csv(f, header=None)
    dfList.append(Dataframes)

concatDf = pd.concat(dfList, axis=0)
# concatDf.columns = DataHeaders
concatDf.to_csv('Combine_files.csv', index=None)

'''
import csv

with open('5ec22961a5533967a888db87.csv', 'r') as fin, open('5ec22961a5533967a888db87-1.csv', 'w', newline='') as fout:

    # define reader and writer objects
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',')

    # write headers
    writer.writerow(next(reader))

    # iterate and write rows based on condition
    for i in reader:
        if int(i[-1]) > 2000:
            writer.writerow(i)
'''