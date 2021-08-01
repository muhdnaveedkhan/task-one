import os
import glob
import pandas as pd
import datetime as dt


'''
# Converting Text files data into CSV file.
os.chdir("/home/naveedkhan/task1_env/weatherfiles/")
extension = 'txt'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index = False, encoding='utf-8-sig')
'''
    
file = r"/home/naveedkhan/task1_env/weatherfiles/combined_csv.csv"
dataFrm = (pd.read_csv(file)) 
dataFrm.sort_values(by=['PKT'], inplace = True, ascending = False)
x= dataFrm.groupby(['PKT'])
dataFrm.head(10)

dataFrm['Year'] = pd.DatetimeIndex(dataFrm['PKT']).year
dataFrm['Month'] = pd.DatetimeIndex(dataFrm['PKT']).month
dataFrm['Date'] = pd.DatetimeIndex(dataFrm['PKT']).day
dataFrm = dataFrm[['PKT','Max TemperatureC', 'Min TemperatureC', 'Max Humidity',
                   ' Mean Humidity', ' Min Humidity','Year','Month','Date']]
min_temp = []
max_temp = []
min_Humidity = []
max_Humidity = []

min_temp.clear()
max_temp.clear()
min_Humidity.clear()
max_Humidity.clear()

print ("Please Enter Report Number:" \
              "\n 1: For Min/Max Temperature & Humidity " \
              "\n 2: For Average highest Temperature, Average Lowest Temperature, Average Mean Humidity " \
              "\n 3: For the Highest and lowest Temperature on Each Day ")
option = input("Enter Your Choice : ")

if (option == '1'):
    print("\n You have selected option 1.\n")
    min_temp.clear()
    max_temp.clear()
    min_Humidity.clear()
    max_Humidity.clear()
    year = int(input('Enter Year : '))
    year = int(year)
    mask = dataFrm['Year'] == year
    include = dataFrm[mask]
    exclude = dataFrm[~mask]
    min_temp.append(include[include['Min TemperatureC'] == include['Min TemperatureC'].min()])
    max_temp.append(include[include['Max TemperatureC'] == include['Max TemperatureC'].max()])
    min_Humidity.append(include[include[' Min Humidity'] == include[' Min Humidity'].min()])
    max_Humidity.append(include[include['Max Humidity'] == include['Max Humidity'].max()])
    
    min_t = min(min_temp)
    max_t = max(max_temp)
    min_hum = min(min_Humidity)
    max_hum = max(max_Humidity)
    
    max_t1 = max_t['Max TemperatureC'].drop_duplicates()
    max_month = max_temp[0]['Month'].drop_duplicates()
    max_date = max_temp[0]['Date']
    
    min_t1 = min_t['Min TemperatureC'].drop_duplicates()
    # min_month = min_temp[0]['Month'].drop_duplicates()
    # min_date = min_temp[0]['Date'].drop_duplicates()
    
     
    # print(min_hum[' Min Humidity'].drop_duplicates())
    max_hum = max_hum['Max Humidity'].drop_duplicates()
    # month_max_hum = max_hum[0]['Month'].drop_duplicates()
    # month_max_hum = max_hum[0]['Date'].drop_duplicates()
        
    
    print('\n--------------------------------------------\n')
    print(f'Highest: {max_t1}C on {max_month} {max_date}')
    # print(f"Lowest: {min_temp[0]['Min TemperatureC']}C on {min_temp[0]['Month']} {min_temp[0]['Date']}")
    # print(f"Humidity: {max_Humidity[0]['Max Humidity']}% on {max_Humidity[0]['Month']} {max_Humidity[0]['Date']}")
    print('\n--------------------------------------------\n')
    
elif (option == '2'):
    print("\n You have selected option 2.\n")
    year = int(input('Enter Year : '))
    year = int(year)
    month = int(input('Enter Month : '))
    month = int(month)
    maskForMonth = dataFrm['Month'] == month
    maskForYear = dataFrm['Year'] == year
    include = dataFrm[maskForMonth & maskForYear]
    exclude = dataFrm[~maskForMonth & ~maskForYear]
    
    print("Highest Average:", (include["Max TemperatureC"].mean()))
    print("Lowest Average:", (include["Min TemperatureC"].mean()))
    print("Average Mean Humidity:", (include[" Mean Humidity"].mean()))

    
    '''
    max_temp.clear()
    min_Humidity.clear()
    max_Humidity.clear()
    
    max_temp.append(include[include['Max TemperatureC'] == include['Max TemperatureC'].max()])
    
    # print(type(max_temp))
    # print(max_temp)
    
    # min_Humidity.append(include[include[' Min Humidity'] == include[' Min Humidity'].min()])
    # max_Humidity.append(include[include['Max Humidity'] == include['Max Humidity'].max()])
    print('Maximum Temp:', max_temp[0])
    # print('Minimum Humidity:',min_Humidity[0])
    # print('Max Humidity:',max_Humidity[0]) 
    # time.sleep(5)
    
    # print("Highest Average: 39C")
    # print("Lowest Average: 18C ")
    # print("Average Mean Humidity: 71%")
    
    
    '''
    
        
'''            
elif (option == '3'):
    # import time
    print("\n You have selected option 3.\n")
    
    for year in range(2004,2016,1):
        mask = dataFrm['Year']==year
        include = dataFrm[mask]
        exclude = dataFrm[~mask]
        min_temp.clear()
        min_Humidity.clear()
        max_Humidity.clear()
        
        min_temp.append(include[include['Min TemperatureC'] == include['Min TemperatureC'].min()])
       # min_Humidity.append(include[include[' Min Humidity'] == include[' Min Humidity'].min()])
       # max_Humidity.append(include[include['Max Humidity'] == include['Max Humidity'].max()])
        print('Maximum Temp:',min_temp[0])
       # print('Minimum Humidity:',min_Humidity[0])
       # print('Max Humidity:',max_Humidity[0]) 
        # time.sleep(5)
'''





# DataFrame Attributes and Methods to Analyze data
# print(dataFrm)
# print( dataFrm.dtypes)
# print( dataFrm.shape)
# print( dataFrm.index )
# print ( dataFrm.columns )
# print (dataFrm.head(2) )
# print(dataFrm.tail())
# print( dataFrm['PKT'].unique() )
# print( dataFrm.nunique())
# print( dataFrm.count())
# print( dataFrm['PKT'].value_counts() )
# print( dataFrm.info() )
# print( dataFrm.isnull() )
# print( dataFrm.isnull().sum())
# print( len(dataFrm['Max TemperatureC'].unique()) )
# print( dataFrm['Year'] == 2005)
# print( dataFrm.groupby('Year').get_group(2008) )
# print( dataFrm[' Mean Humidity'].mean() ) # calculate mean value
# print( dataFrm[' Mean Humidity'].std() ) # calculate standard deviation
# print( dataFrm[' Mean Humidity'].var() ) # calculate variance
# print( dataFrm)
# print( dataFrm.groupby('Year').min() )


'''
1. For a given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.
weatherman.py /path/to/files-dir -e 2002
Highest: 45C on June 23
Lowest: 01C on December 22
Humidity: 95% on August 14
2. For a given month display the average highest temperature, average lowest temperature, average mean humidity.
weatherman.py /path/to/files-dir -a 2005/6
Highest Average: 39C
Lowest Average: 18C
Average Mean Humidity: 71%
3. For a given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.
weatherman.py /path/to/files-dir -c 2011/03
March 2011
01 +++++++++++++++++++++++++ 25C
01 +++++++++++ 11C
02 ++++++++++++++++++++++ 22C
02 ++++++++ 08C
'''