import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

dat=pd.read_csv(path/Train_image_info2.csv",header=[0],engine='python')
d={} #dictionary that has key=image, value a list of [number obj class1, number obj class2 and estimated population]
for ind in dat.index:
    if(dat["Image"][ind]) not in d:
        d[dat["Image"][ind]]=[0,0,0]        
acc=0.75 
for ind in dat.index:
    a=(dat['xmin'][ind],dat['ymin'][ind])
    b=(dat['xmax'][ind],dat['ymin'][ind])
    c=(dat['xmin'][ind],dat['ymax'][ind])
    base = distance.euclidean(a, b)*0.5    #from pixels to meters
    height = distance.euclidean(a, c)*0.5
    area= base*height*acc  
    if dat["Class"][ind]==1: #large block buildings
        d[dat["Image"][ind]][0]+=1
        d[dat["Image"][ind]][2]+= round(area*0.065,0)
    elif dat["Class"][ind]==2: #small villas
        d[dat["Image"][ind]][1]+=1
        d[dat["Image"][ind]][2]+= round(area*0.010,0)

plt.figure(figsize=(25,15))
for key in d:
    p=plt.scatter(key, d[key][2])
plt.title('ESTIMATED POPULATION OF ANALYZED IMAGES',fontsize=30)
plt.ylabel('Population',fontsize=25)
p.axes.get_xaxis().set_visible(False)
plt.show()
