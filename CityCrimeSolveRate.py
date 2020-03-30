# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 02:17:21 2020

@author: Ashish
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#from pylab import rcParams

import numpy as np
import pandas as pd 

data1=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\database.csv')

data2=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\database.csv'\
                  ,usecols=['State','City','Crime Solved'])

data3=data2.head()

total=data2['City'].value_counts().to_dict()

data2=data2[data2['Crime Solved']!='No']

cities=data2['City'].unique().tolist()

solved=data2['City'].value_counts().to_dict()


solverate=dict()
for i in cities:
    solverate[i]=float("{0:.2f}".format((solved[i]/total[i])*100))

solveratedata=pd.DataFrame(columns=['City','Solve Rate'])
solveratedata['City']=list(solverate.keys())
solveratedata['Solve Rate']=list(solverate.values())

solveratedata=solveratedata[solveratedata['Solve Rate']!=100]

solveratedata.index=np.arange(len(solveratedata['City']))
#Plotting left
coordinates=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\cleandatabase.csv')

solveratedata['Lat']='?'
solveratedata['Long']='?'

for i in range(len(solveratedata['City'])):
               city=solveratedata['City'][i]
               index1=coordinates[coordinates['Cities']==city].index
               if index1.size!=0:
                   lat=coordinates['Lat'][index1[0]]
                   long=coordinates['Long'][index1[0]]
                   solveratedata['Lat'][i]=lat                
                   solveratedata['Long'][i]=long 

solveratedata=solveratedata[solveratedata['Lat']!='?']

lowerlong=-161.75583 
lowerlat=19.50139 
upperlong=-68.01197  
upperlat=64.85694 

map1=Basemap(projection='merc',resolution='l',llcrnrlon=lowerlong,llcrnrlat=lowerlat,\
              urcrnrlon=upperlong,urcrnrlat=upperlat,area_thresh=1000)   
map1.drawcoastlines(linewidth=1.2)
map1.drawcountries(linewidth=1.2)
map1.drawstates(color='blue',linewidth=0.1)
#map1.drawcounties()
#map1.drawlsmask(land_color='orange',ocean_color='skyblue')
#map1.bluemarble()
x=list(solveratedata.Long)
y=list(solveratedata.Lat)

xs,ys=map1(x,y)

solveratedata['xmerc']=xs
solveratedata['ymerc']=ys

solveratedata['Solve Rate'].describe()

for j,i in solveratedata.iterrows():
    if i['Solve Rate']<65:
        map1.plot(i.xmerc,i.ymerc,markerfacecolor='red',markeredgecolor='pink',marker='o',markersize=5,alpha=1)
    elif i['Solve Rate']>=65 and i['Solve Rate']<75:
        map1.plot(i.xmerc,i.ymerc,markerfacecolor='yellow',markeredgecolor='pink',marker='o',markersize=5,alpha=0.8)
    #else:
    #    map1.plot(i.xmerc,i.ymerc,markerfacecolor='green',markeredgecolor='pink',marker='o',markersize=5,alpha=0.5)
    
plt.show()
