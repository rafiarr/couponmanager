import csv
import os

class CSVReader:

    fileName = ''

    def setFileName(self,newFileName):
        self.fileName = newFileName

    def readCsv(self):
        datas = []
        fileName = self.fileName
        isValid = self.__validateFileName(fileName)
        if (isValid == False):
            # print("False")
            return datas
        else :
            # print(fileName)
            with open(fileName, 'r') as fileCsv:
                csvObjcet = csv.reader(fileCsv,delimiter=',')
                for row in csvObjcet:
                    datas.append(row)

            return datas

    def __validateFileName(self,fileName):
        if (os.path.isfile(fileName) == True):
            return True
        else:
            return False

# csvReader = CSVReader("nafiar.csv")
# print(csvReader.readCsv())