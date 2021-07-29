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
        
# print(input_data)

df = pd.DataFrame(input_data)

print( df.shape )
