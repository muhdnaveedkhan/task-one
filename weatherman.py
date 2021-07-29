import os
import glob
import pandas as pd
import datetime as dt

os.chdir("/home/naveedkhan/task1_env/weatherfiles/")
extension = 'txt'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat( [pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv( "combined_csv.csv", index = False, encoding='utf-8-sig')

import pandas as pd

class weather:
    
    def main(self):
        # Retrieving data from CSV file
        file = r"/home/naveedkhan/task1_env/weatherfiles/combined_csv.csv"
        dataFrm = (pd.read_csv(file))
        '''
        dataFrm.sort_values(by = ['PKT'], inplace=True, ascending=False)
        x = dataFrm.groupby(['PKT'])
        dataFrm.head(10)
        
        # Required four columns
        dataFrm['year'] = pd.DatetimeIndex(dataFrm['PKT']).year
        dataFrm['month'] = pd.DatetimeIndex(dataFrm['PKT']).month
        dataFrm['date'] = pd.DatetimeIndex(dataFrm['PKT']).day
        dataFrm = dataFrm[['PKT','Max TemperatureC', 'Min TemperatureC', 'Max Humidity',
                ' Min Humidity',]]
       
        min_temp = []
        max_temp = []
        min_Humidity = []
        max_Humidity = []
        min_temp.clear()
        max_temp.clear()
        min_Humidity.clear()
        max_Humidity.clear()
        
        print( '---------------------------------------------------------------')
        print('Year', year)
        print("Min Temp", min_temp[0]['Min TemperatureC'])
        print("Max Temp", max_temp[0]['Max TemperatureC'])
        print("Min Humidity", min_temp[0]['Min Humidity'])
        print("Max Humidity", max_temp[0]['Max Humidity'])
        
        print ("Please Enter Report Number:" \
                      "\n 1: for Annual Max/Min Temperature" \
                      "\n 2: for Hottest day of each year" \
                      "\n 3: for coldest day of each year")
        
        option = input()
        
        if (option == '1'):
            year = input('Enter year')
            mask = dataFrm['year'] == int(year)
            include = dataFrm[mask]
            exclude = dataFrm[~mask]
            min_temp.append(include[include['Min TemperatureC'] == include['Min TemperatureC'].min()])
            max_temp.append(include[include['Max TemperatureC'] == include['Max TemperatureC'].max()])
            min_Humidity.append(include[include[' Min Humidity'] == include[' Min Humidity'].min()])
            max_Humidity.append(include[include['Max Humidity'] == include['Max Humidity'].max()])
            

        if (option == '2'):
            for year in range(2004,2016,1):
                
                mask = dataFrm['year']==int(year)
                include = dataFrm[mask]
                exclude = dataFrm[~mask]
                
                print("max Temp",include[include['Max TemperatureC'] == include['Max TemperatureC'].max()])
                print("min Humidity",include[include[' Min Humidity'] == include[' Min Humidity'].min()])
                print("max humidity",include[include['Max Humidity'] == include['Max Humidity'].max()])
                
                
        if ( option == '3' ) :
            for year in range(2004,2016,1):    
        
                mask = dataFrm['year']==int(year)
                include = dataFrm[mask]
                exclude = dataFrm[~mask]            
            
                print("min Temp",min_temp.append(include[include['Min TemperatureC'] == include['Min TemperatureC'].min()]))
                print("min Humidity",include[include[' Min Humidity'] == include[' Min Humidity'].min()])
                print("max humidity",include[include['Max Humidity'] == include['Max Humidity'].max()])
'''        
obj = weather();
obj.main()




# DataFrame Attributes
        # print( dataFrm.shape)
        # print( dataFrm.columns )
        # print( dataFrm.index )
# DataFrame Methods
        # print( dataFrm.info() )
        # print( dataFrm.head() )
        # print( dataFrm.tail() )
        # print( dataFrm.count() )
        # print( dataFrm.describe() )
                