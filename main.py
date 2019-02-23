import os
import csv
from pathlib import Path


print(os.getcwd())

def readCsv(fileName):
    datas = []
    with open(fileName, 'r') as fileCsv:
        csvObjcet = csv.reader(fileCsv,delimiter=',')
        for row in csvObjcet:
            datas.append(row)

    return datas



if __name__ == '__main__':
    newDatas = []
    fileName = os.getcwd() + "\rafiar.csv"
    newDatas = readCsv(fileName)
    print(newDatas)
