import csv
import os
from collections import defaultdict
from datetime import datetime
# os.system('cls')

# Reading data from text files
input_data = {}

# path = os.path.join(os.getcwd(),'weatherfiles/')
 
path = '/home/naveedkhan/task1_env/weatherfiles/'

for files in os.listdir(path):
    if files.endswith(".txt"):
        with open(path + files, "r") as weather:
            read_data = weather.readlines()
            input_file = csv.DictReader( read_data[0:-1] )         
            for row in input_file:
                if row.get('PKT'):
                    date = datetime.strptime( str(row['PKT']), "%Y-%m-%d")
                else:
                    date = datetime.strptime(str(row['PKST']), "%Y-%m-%d")
                input_data.setdefault(date.year, {}).setdefault(date.month, []).append(row)
            weather.close()

# Program logic
min_temp = {}
max_temp = {}
min_humidity = {}
max_humidity = {}

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
'''


'''
def clean(l, key):
    new_list = []
    for d in l:
        value = d.get(key)
        if value:
            new_list.append(d)
    return new_list

#  def find_max(input_dict, key):
#     out_dict = {}
#     for key_year, year in input_dict.items():
#         l = clean(year, key)
#         if l:
#             maximum = max(l, key=lambda x: x[key])
#             out_dict[key_year] = maximum
#         else:
#             out_dict[key_year] = {}
#     return out_dict

def find_min(input_dict, key):
    out_dict = {}
    for key_year, year in input_dict.items():
        l = clean(year, key)
        if l:
            minimum = min(l, key=lambda x: x[key])
            out_dict[key_year] = minimum
        else:
            out_dict[key_year] = {}
    return out_dict
'''