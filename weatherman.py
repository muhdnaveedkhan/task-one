import csv
import os
from collections import defaultdict

from datetime import datetime
from posix import listdir

# path = '/home/naveedkhan/task1_env/weatherfiles/'
# print(os.listdir(path) )


class Weather:
    def main(self):
        # path = raw_input("Enter weather data directory.")
        # path = "C:\Users\Irfan\Desktop\weatherdata\weatherdata\\"
        # path = os.path.join(os.getcwd(),'weatherfiles/') 
        path = '/home/naveedkhan/task1_env/weatherfiles/'
        if not os.path.exists(path):
            print( "Invalid data directory!")
            return
        print( "Please Enter Report Number:" \
              "\n 1: for Annual Max/Min Temperature" \
              "\n 2: for Hottest day of each year" \
              "\n 3: for coldest day of each year")
        option =int(input("Report Number."))

        os.system('cls')
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
                max_humidity_list.append(max(month, key=lambda x: x['Max Humidity']))
                max_humidity[key_year] = max_humidity_list
                min_humidity_list.append(min(month, key=lambda x: x[' Min Humidity']))
                min_humidity[key_year] = min_humidity_list
                
        min_temp = Weather.find_min(min_temp, 'Min TemperatureC')
        max_temp = Weather.find_max(max_temp, 'Max TemperatureC')
        
        min_humidity = Weather.find_min(min_humidity, ' Min Humidity')
        max_humidity = Weather.find_max(max_humidity, 'Max Humidity')
        
        if option == 1:
            output_data = Weather.create_output(min_temp, max_temp, min_humidity, max_humidity)
            Weather.annual_min_max(output_data)
        elif option == 2:
            print( "\n\n Hottest day of each year:\n")
            Weather.hottest_day(max_temp)
        elif option == 3:
            print( "\n\n Coldest day of each year:\n")
            Weather.coldest_day(min_temp)
        else:
            print( 'weatherman', path)

    @staticmethod
    def annual_min_max(output_data):
        print( Weather.pad_value('Year', 10), Weather.pad_value('MIN Temp', 10), \
            Weather.pad_value('MAX Temp', 10), Weather.pad_value('MAX Humidity', 15), \
            Weather.pad_value('MIN Humidity', 10))
        print( '---------------------------------------------------------------')
        for key_year, year in output_data.items():
            min_t = year[0].get('Min TemperatureC')
            max_t = year[1].get('Max TemperatureC')
            min_hum = year[2].get(' Min Humidity')
            max_hum = year[3].get('Max Humidity')
            print( Weather.pad_value(str(key_year), 12), Weather.pad_value(str(min_t), 10), \
                Weather.pad_value(str(max_t), 12), Weather.pad_value(str(max_hum), 15), \
                Weather.pad_value(str(min_hum), 10))

    @staticmethod
    def hottest_day(output_data):
        print( Weather.pad_value('Year', 10), Weather.pad_value('Date', 10), \
            Weather.pad_value('Temp', 10))
        print( '------------------------------------------------')
        for key_year, year in output_data.items():
            if year.get('PKT'):
                date = year.get('PKT')
            else:
                date = year.get('PKST')
            max_t = year.get('Max TemperatureC')
            print( Weather.pad_value(str(key_year), 8), Weather.pad_value(str(date), 12), \
                Weather.pad_value(str(max_t), 12))

    @staticmethod
    def coldest_day(output_data):
        print( Weather.pad_value('Year', 10), Weather.pad_value('Date', 10), \
            Weather.pad_value('Temp', 10))
        print( '------------------------------------------------')
        for key_year, year in output_data.items():
            if year.get('PKT'):
                date = year.get('PKT')
            else:
                date = year.get('PKST')
            max_t = year.get('Max TemperatureC')
            print( Weather.pad_value(str(key_year), 8), Weather.pad_value(str(date), 12), \
                Weather.pad_value(str(max_t), 12))

    @staticmethod
    def pad_value(text, pad):
        return text.ljust(pad)

    @staticmethod
    def create_output(*dicts):
        output_data = defaultdict(list)
        for d in dicts:
            for key, value in d.items():
                output_data[key].append(value)
        return output_data

    @staticmethod
    def clean(l, key):
        new_list = []
        for d in l:
            value = d.get(key)
            if value:
                new_list.append(d)
        return new_list

    @staticmethod
    def find_min(input_dict, key):
        out_dict = {}
        for key_year, year in input_dict.items():
            l = Weather.clean(year, key)
            if l:
                minimum = min(l, key=lambda x: x[key])
                out_dict[key_year] = minimum
            else:
                out_dict[key_year] = {}

        return out_dict

    @staticmethod
    def find_max(input_dict, key):
        out_dict = {}
        for key_year, year in input_dict.items():
            l = Weather.clean(year, key)
            if l:
                maximum = max(l, key=lambda x: x[key])
                out_dict[key_year] = maximum
            else:
                out_dict[key_year] = {}
        return out_dict


Weather().main()
