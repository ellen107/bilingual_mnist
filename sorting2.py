import os
from PIL import Image
import shutil

path = r'/Users/echen/Documents/DataScience/DS340W/mnist_png/testing/'
labels = [0,1,2,3,4,5,6,7,8,9]

for l in labels:
     for filename in os.listdir(path+str(l)):
         shutil.move(path+str(l)+'/'+filename, r'/Users/echen/Documents/DataScience/DS340W/bilingual/chinese_mnist/'+ str(l))