from PIL import Image

import os

path = r'/Users/echen/Documents/DataScience/DS340W/chinese_mnist/data/data/'

for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        im = Image.open(path+filename).resize((28,28))
        name = filename[:-4]
        im.save(r'/Users/echen/Documents/DataScience/DS340W/bilingual/chinese/'+ name+'.png')
        
        
        continue
    else:
        continue