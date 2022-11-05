import os 
labels = ["0", "1", "2", "3","4", "5", "6","7", "8","9","10","100","1000","10000","100000000"]
dir_path = "/Users/echen/Documents/DataScience/DS340W/bilingual/bilingual_datanew"

for i in labels:
    path = os.path.join(dir_path,i)
    os.mkdir(path)
