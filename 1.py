import os
from datetime import datetime
# print( dir(os) )
# print( os.getcwd() )
# print( os.getcwdb() )
# os.chdir( '/home/naveedkhan/task1_env/task1' )
# print( os.getcwd() )
# os.chdir( '/home/naveedkhan/task1_env' )
# print( os.getcwd() )
# print( os.listdir() )
# os.mkdir("khan")
# os.makedirs("khan-2/sub-dir-1")
# print( os.listdir() )
# os.rmdir('khan')
# os.removedirs('khan/sub-dir-1')
# print( os.listdir() )
# os.chdir('/home/naveedkhan/task1_env/weatherfiles')
# print( os.getcwd() )
# mod_time = os.stat('/home/naveedkhan/task1_env/weatherfiles/Murree_weather_2004_Aug.txt').st_mtime
# print( datetime.fromtimestamp(mod_time) )
# os.walk()

# data_folder = os.getcwd()
# for dirpath, dirname, filename in os.walk('/home/naveedkhan/task1_env'):
#     print("Current path : ", dirpath)
#     print("Directories : ", dirname)
#     print("Files : ", filename)
#     print()
'''
print( os.environ.get('HOME') )
# 'test.txt' -> filename
# file_path = os.environ.get('HOME') + 'test.txt'
file_path = os.path.join(os.environ.get('HOME') , 'test.txt')
print( file_path )
'''
print( os.path.basename('/temp/test.txt') ) # test.txt
print( os.path.dirname('/temp/test.txt') ) # /temp
print( os.path.split('/temp/test.txt') ) # ('/temp', 'test.txt')
print ( os.path.exists('/temp/test.txt') ) # False or True
print ( os.path.isdir('/temp/test.txt') ) # False or True
print ( os.path.isfile('/temp/test.txt') ) # False or True
print ( os.path.splitext('/temp/test.txt') ) # ('/temp/test', '.txt')

print ( dir(os.path ) )