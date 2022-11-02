import os
from PIL import Image
import shutil

path = r'/Users/echen/Documents/DataScience/DS340W/bilingual/chinese/'

code_list = {'1': 0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8,'10':9, '11':10, '12':100, '13': 1000, '14':10000, '15':100000000}

for filename in os.listdir(path):
    if filename.endswith('.png'):
        code = filename.split("_")[-1]
        code2 = code.split(".")[0] 
    
        shutil.move(path+filename, '/Users/echen/Documents/DataScience/DS340W/bilingual/'+str(code_list[code2]))