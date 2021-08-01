import csv
import os
import numpy
import pandas as pd
from collections import defaultdict
from datetime import datetime
# os.system('cls')

'''
# Reading data from text files
# path = os.path.join(os.getcwd(),'weatherfiles/')
# path = raw_input("Enter weather data directory.")

path = '/home/naveedkhan/task1_env/weatherfiles/'
input_data = {}

for files in os.listdir(path):
    # print(path+files)
    dataFrm = pd.read_csv(path + files, sep=",")    

# print( dataFrm.dtypes ) 

column = dataFrm['Max TemperatureC']
max_value = column.max()
print(max_value)
'''

# path = os.path.join(os.getcwd(),'weatherfiles/')
# path = raw_input("Enter weather data directory.")
path = '/home/naveedkhan/task1_env/weatherfiles/'

input_data = {}

for files in os.listdir(path):
    if files.endswith(".txt"):
        with open(path + files, "r") as weather:
            d = weather.readlines()
            input_file = csv.DictReader(d[0:-1])
            for row in input_file:
                if row.get('PKT'):
                    date = datetime.strptime(str(row['PKT']), "%Y-%m-%d")
                else:
                    date = datetime.strptime(str(row['PKST']), "%Y-%m-%d")
                input_data.setdefault(date.year, {}).setdefault(date.month, []).append(row)
        weather.close()
  
#-------- Functions ---------------
# Pass a list to this function to check for maximum number
def max_check(input_list):
  max_val = input_list[0] 
  for check in input_list: 
    if check > max_val: 
      max_val = check 
  return max_val

# Pass a list to this function to check for minimum number
def min_check(input_list):
  min_val = input_list[0] 
  for check in input_list: 
    if check < min_val: 
      min_val = check 
  return min_val
#-------- End Functions ---------------
min_temp = {}
max_temp = {}
max_humidity = {}
min_humidity = {}
    
for key_year, year in input_data.items():
    min_temp_list = []
    max_temp_list = []
    min_humidity_list = []
    max_humidity_list = []
    
    for key_month, month in year.items():
        
        min_temp_list.append(min(month, key=lambda x: x['Min TemperatureC']))
        min_temp[key_year] = min_temp_list     
        
        max_temp_list.append(max(month, key=lambda x: x['Max TemperatureC']))
        max_temp[key_year] = max_temp_list
        
        min_humidity_list.append(min(month, key=lambda x: x[' Min Humidity']))
        min_humidity[key_year] = min_humidity_list
        
        max_humidity_list.append(max(month, key=lambda x: x['Max Humidity']))
        max_humidity[key_year] = max_humidity_list
        
        
        # min_temp = find_min(min_temp, 'Min TemperatureC')
        # max_temp = Weather.find_max(max_temp, 'Max TemperatureC')
        # max_humidity = Weather.find_min(max_humidity, 'Max Humidity')
        # min_humidity = Weather.find_max(min_humidity, ' Min Humidity')


print ("Please Enter Report Number:" \
    "\n 1: For Min/Max Temperature & Humidity " \
    "\n 2: For Average highest Temperature, Average Lowest Temperature, Average Mean Humidity " \
    "\n 3: For the Highest and lowest Temperature on Each Day ")
option = input("Enter Your Choice : ")

if (option == '1'):
    print("\n You have selected option 1.\n")
    year = int(input('Enter Year : '))
    year = int(year)
    
    # print( min_temp[year] )
    # print( type ( min_temp[year] ) )
    # print( min_temp[year][0] )
    # print( type ( min_temp[year][0] ) )
    min_TC = [] 
    for forecast in  min_temp[year]:
        min_t = forecast['Min TemperatureC']
        min_TC.append( min_t )
    min_TC_list = [int(i) for i in min_TC]
   
    max_TC = [] 
    for forecast in  max_temp[year]:
        max_t = forecast['Max TemperatureC']
        max_TC.append( max_t )
    max_TC_list = [int(i) for i in max_TC]
   
    max_hum = [] 
    for forecast in  max_humidity[year]:
        max_h = forecast['Max Humidity']
        max_hum.append( max_h )
    max_hum_list = [int(i) for i in max_hum]

    print('\n--------------------------------------------\n')
    print(f'Highest: {max(max_TC_list)}C on Month Date')
    print(f"Lowest: {min(min_TC_list)}C on Month Date")
    print(f"Humidity: {max(max_hum_list)}% on Month Date")
            
    print("\n-------------end option 1----------------\n")
'''
print( "Please Enter Report Number:" \
    "\n 1: for Annual Max/Min Temperature" \
    "\n 2: for Hottest day of each year" \
    "\n 3: for coldest day of each year")

option = input("Report Number : ")      
        
if option is 1:
    output_data = Weather.create_output(min_temp, max_temp, min_humidity, max_humidity)
    Weather.annual_min_max(output_data)

elif option is 2:
    print( "\n\n Hottest day of each year:\n")
    Weather.hottest_day(max_temp)
elif option is 3:
    print("\n\n Coldest day of each year:\n")
    Weather.coldest_day(min_temp)
else:
    print('Weatherman', path)   
'''




# print( input_data[2004])
# print( type (input_data[2004]) )

# print( input_data[2004][7])
# print( type( input_data[2004][7] ))

# print( input_data[2004][7][0])
# print( type( input_data[2004][7][0] ) )

# print( input_data[2004][7][0]['PKT'])
# print( type(input_data[2004][7][0]['PKT'] ))




# print(date.day)
# print("\n--------------------------------------\n")
# for key in input_data.keys():
#     print(key , "----------", input_data[key])
#     print("\n<<<<<<<<<<<<<<<<<-------------------------------------->>>>>>>>>>>>\n")
#     break
# print('\\ END LOOP')
# for key_year, year in input_data.items():
#     for key_month, month in year.items():
#         print("\n<<<<<<<<<<<<<<<<<-------------------------------------->>>>>>>>>>>>\n")
#         print('KEY => ', key_month , "Value => ", month) 
#         break