import os
from csv_reader import CSVReader

class Coupon:

    couponDeirectory = ''
    couponDatas = []
    
    def __init__(self,couponDeirectory):
        self.couponDeirectory = couponDeirectory
        self.csvReader = CSVReader()
        self.__generateCouponDatas()

    def __generateCouponDatas(self):
        filesDirectory = self.couponDeirectory
        for dirname, dirnames, filenames in os.walk(filesDirectory):
            # print path to all filenames.
            for filename in filenames:
                fileNamePath = os.path.join(dirname, filename)
                fileNamePath = os.path.normpath(fileNamePath)
                filename = filename.split('.')[0]
                fileDatas = self.__getCSVData(fileNamePath)
                couponData = []
                couponData.append(filename)
                couponData.append(fileDatas)
                self.couponDatas.append(couponData)

    def __getCSVData(self,fileNamePath):
        self.csvReader.setFileName(fileNamePath)
        return self.csvReader.readCsv()

    def getCouponDatas(self):
        return self.couponDatas

if __name__ == "__main__":
    couponDeirectory = os.path.join(os.getcwd(),"CouponFiles")
    # print(os.getcwd())
    # print(couponDeirectory)
    # print(os.path.normpath(couponDeirectory))
    couponDeirectoryPath = os.path.normpath(couponDeirectory)
    coupon = Coupon(couponDeirectoryPath)
    couponDatas = coupon.getCouponDatas()
    print(couponDatas)
