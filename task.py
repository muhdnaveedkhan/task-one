from datetime import datetime
import pandas as pd
import numpy as np
import glob
from colorama import Fore

# from termcolor import colored
# import os
dirPath = glob.glob('/home/naveedkhan/task1_env/weatherfiles/*.txt')
dataFrame = pd.concat(pd.read_csv(file) for file in dirPath)
dataFrame[["year", "month", "day"]] = dataFrame["PKT"].str.split("-", expand = True)
dataFrame.reset_index(drop = True, inplace = True)

class Weather:
            
    def findYearWise(self, year):
        yearPD = dataFrame.loc[(dataFrame['year'] == year)]

        maxTemp = yearPD['Max TemperatureC'].max()
        maxTempIndex = yearPD[yearPD['Max TemperatureC'] == maxTemp].index.values
        maxMonth = yearPD.loc[maxTempIndex, 'month'].values[0]
        maxMonthObject = datetime.strptime(maxMonth, "%m")
        maxMonthName = maxMonthObject.strftime("%B")
        maxDay = yearPD.loc[maxTempIndex, 'day'].values[0]

        minTemp = yearPD['Min TemperatureC'].min()
        minTempIndex = yearPD[yearPD['Min TemperatureC'] == minTemp].index.values
        minMonth = yearPD.loc[minTempIndex, 'month'].values[0]
        minMonthObject = datetime.strptime(minMonth, "%m")
        minMonthName = minMonthObject.strftime("%B")
        minDay = yearPD.loc[minTempIndex, 'day'].values[0]

        maxHumidity = yearPD['Max Humidity'].max()
        maxHumidityIndex = yearPD[yearPD['Max Humidity'] == maxHumidity].index.values
        maxHumidityMonth = yearPD.loc[maxHumidityIndex, 'month'].values[0]
        maxHumidityMonthObject = datetime.strptime(maxHumidityMonth, "%m")
        maxHumidityMonthName = maxHumidityMonthObject.strftime("%B")
        maxHumidityDay = yearPD.loc[maxHumidityIndex, 'day'].values[0]

        print(' Highest : ' + str(maxTemp) + ' C ' + ' on ' + maxMonthName + ' ' + maxDay)
        print(' Lowest : ' + str(minTemp) + ' C ' + ' on ' + minMonthName + ' ' + minDay)
        print(' Humidity : ' + str(maxHumidity) + ' % ' + ' on ' + maxHumidityMonthName + ' ' + maxHumidityDay)

    def findYearMonthWise(self, year,month):
        yearPD = dataFrame.loc[(dataFrame['year'] == year) & (dataFrame['month'] == month)]

        maxTemp = yearPD['Mean TemperatureC'].max()
        minTemp = yearPD['Mean TemperatureC'].min()
        maxHumidity = yearPD['Max Humidity'].max()

        print(' Highest Average: : ' + str(maxTemp) + ' C ')
        print(' Lowest Average : ' + str(minTemp) + ' C ')
        print(' Average Mean Humidity : ' + str(maxHumidity) + ' % ')

    def findYearMonthDayWise(self, year,month):
        yearPD = dataFrame.loc[(dataFrame['year'] == year) & (dataFrame['month'] == month)]
        yearPD.sort_values(by=['day'])

        for i in yearPD['day']:
            tempDF = dataFrame.loc[(dataFrame['day'] == i)]
            maxTemp = tempDF['Max TemperatureC'].max()
            minTemp = tempDF['Min TemperatureC'].min()
            
            print(Fore.WHITE + i, end='')

            for j in range(0,int(maxTemp)):
                print(Fore.RED + '+', end='')
            print(maxTemp)
            
            print(Fore.WHITE + i, end='')
            
            for k in range(int(minTemp), 0):
                print(Fore.BLUE + '+',  end='')
            print(minTemp)
    def main(self):
        print ("Please Enter Report Number:" \
                "\n 1: For Min/Max Temperature & Humidity " \
                "\n 2: For Average highest Temperature, Average Lowest Temperature, Average Mean Humidity " \
                "\n 3: For the Highest and lowest Temperature on Each Day ")

        option = input("Enter Your Choice : ")

        if (option == '1'):
            print("\n You have selected option 1.\n")
            year = input('Enter Year : ')
            self.findYearWise(year)
        elif (option == '2'):
            print("\n You have selected option 2.\n")
            year = input('Enter Year : ')
            month = input('Enter Month : ')
            self.findYearMonthWise(year,month)
        elif (option == '3'):
            print("\n You have selected option 3.\n")
            year = input('Enter Year : ')
            month = input('Enter Month : ')
            self.findYearMonthDayWise(year, month)
        else:
            print('Weatherman', dirPath)  
                

# Main Program
weather = Weather()
weather.main()
        
