# f = open('test.txt', 'r')
# print( f.name )
# print( f.mode )
# print( f.read() )
# print( f.readline() ) #read a single line only
# print( f.readlines() ) #read entire contents of file
# f.close() 
# ------------------------- Program must close the opened file explicitly-----------------

# with open('test.txt', 'r') as f:
    # print( f.name )
    # print( f.mode )
    # print( f.read() )
    # print( f.readline() ) #read a single line only
    # print( f.readlines() ) #read entire contents of file
    
    # f_content = f.readline()
    # print(f_content)
    
    # for line in f:
    #     print(line, end='')
    
# ------------------------- Min/Max values in dictionary-----------------
dict = {
    'key1' : 2132,
    'key2' : 435,
    'key3' : 376,
    'key4' : 870,
    'key5' : 358,
    'key6' : 607
    }

# print ( min(dict.values()) )

# print( dict.keys() )
# for key in dict.keys():
#     print(key)

# print( dict.values() )
# for value in dict.values():
#     print(value)

# print( dict.items() )
# for key, value in dict.items():
#     print(key , '<=>' , value)

# print( dict['key9']) # if key not exist it through an Error:- KeyError: 'key9'
# print( dict.get('key9') ) # if key not exist it returns None
# print( dict.get('key9', 'Not Found!') ) # if key not exist it returns default_value


# key_min = min(dict.keys(), key=(lambda k: dict[k]) )
# key_max = max(dict.keys(), key=(lambda k: dict[k]) )
# print( key_min )
# print( key_max )
# print( dict[key_min] )
# print( dict[key_max] )



'''
filter1 = {key:value for key,value in dict.items() if value < 50 }
print( filter1 )
filter2 = {key:value for key,value in dict.items() if value >= 50}
print( filter2 )
'''
# min_value = min(dict, key = lambda x : dict[x])

# for key in dict:
#     print(key , '=>' , dict[key])


# Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# sampleDict = dict(zip(keys, values))
# print(sampleDict)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)



#Get the key of a minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
minV = min(sampleDict.values())

for k,v in sampleDict.items():
  if  minV == v:
    print(k)
    break
