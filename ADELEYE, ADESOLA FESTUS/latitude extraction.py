""" Name:ADELEYE ADESOLA FESTUS
 Matric number:EEE/2011/0041
 Course:EEE512 Assignment II"""
import os
fileList = []
class earthQuakeData:
    def __init__(self, time, lat, long_, location):
        self.time = time
        self.lat = lat
        self.long_ = long
        self.location = location
    def getlat(self):
        return self.time

    def getLoc(self):
        return self.location

if __name__ == '__main__':
    fil = open("C:\Users\Adesola\Documents\PythonHomework.txt","w")
    with open("C:\Users\Adesola\Documents\Python Software/2.5_month.csv", "r") as f:
        for each in f.readlines():
            fileList = each.split(",")
            print fileList[1]
            
            e = earthQuakeData(fileList[0], fileList[1], fileList[2], fileList[13] + fileList[14])
            fil.write(e.getLoc() + "\n")
        fil.close()
        
            

