# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:05:04 2020
@author: Ashish Rao
Note: I have used the exact code I carried out for analysing data. 

Problem: Show and plot on a map the areas in the USA where gun violence has been carried out.
         The main objective would be to analyse the plot and derive which region has the most records
         for gun violence
Solution:- 
    Datasets used:
        Homicide Reports (1980-2014) in the USA-
        https://www.kaggle.com/murderaccountability/homicide-reports
    
        US cities database(free)-
        https://simplemaps.com/data/us-cities
    Modules used:
        mpl_toolkits
        matplotlib
        pylab
        pandas
    Description:
        In this program, data will be extracted from two different datasets. Cities and Counties will be linked
        to their co-ordinates(Latitudes and Longitudes). The next step would be to filter the rows in the Homicide
        Reports dataset according to the weapon used by the perpetrator. We will consider the weapon to be guns only.
        All other weapons are to be excluded. In the end, the cities and counties with gun violence in records are
        to be plotted on a map. Analysis can then be carried out. 
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

from pylab import rcParams

rcParams['figure.figsize']=(14,10)

#import numpy as np
import pandas as pd

""" STEP 1 
(GETTING CO-ORDINATES FOR PLOTTING) 
We have 2 datasets present. 
First one contains the Homicide reports from 1980-2014 with data about reports which includes: 
City,State,Weapon used by Perpetrator and other parameters which we aren't using in this program. 
Homicide Reports Dataset Path: A:\\Ashish\\TestingProjects\\Datasets\\Homicide Reports (1980-2014)\\database.csv
Second one contains the co-ordinates of all the counties and cities (alongwith states) in the USA.
It contains other parameters too but we won't use them.
US Cities Co-ordinates Dataset Path:A:\\Ashish\\TestingProjects\\Datasets\\Homicide Reports (1980-2014)\\simplemaps_uscities_basicv1.6\\uscities.csv

The main objective in this step is to link the co-ordinates to the cities in the Homicide Reports dataset
from the US Cities Co-ordinates Dataset.
This step doesn't directly add the co-ordinates in the Homicide Reports dataset instead it creates another csv
file. This step can be avoided if needed. 
*** OPTIONAL ***

(EXECUTE ONLY ONCE TO MAKE THE CSV FILE 
AFTER THAT COMMENT EVERYTHING IN STEP 1): 
(This step will save time for future execution)

****************  
"""
    
#murderdata1=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\database.csv',\
#                  index_col=0,na_values=['?'],usecols=['City','State'])
#citiesdata=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\simplemaps_uscities_basicv1.6\uscities.csv'\
#                        usecols=['lat','lng','state_name','county_name','city'] )

#murderdata2=murderdata1.iloc[:10000]
#murdercities=sorted(list(murderdata1['City'].value_counts().keys()))

#murderstates=[]

#for i in murdercities:
#    indexi=murderdata1[murderdata1['City']==i].index
#    if indexi.size!=0:
#        murderstates.append(murderdata1['State'][indexi[0]])
#    else:
#        murderstates.append('?')

#lat=[]
#long=[]

#for i in range(len(murdercities)):
#    c=murdercities[i]
#    s=murderstates[i]
#    k=0
#    indexi2=citiesdata[((citiesdata['city']==c) & (citiesdata['state_name']==s)) | ((citiesdata['county_name']==c) & (citiesdata['state_name']==s)) ].index
#    if indexi2.size!=0:
#        lat.append(citiesdata['lat'][indexi2[0]])
#        long.append(citiesdata['lng'][indexi2[0]])
#    else:
#        lat.append('?')
#        long.append('?')
#    
    
#murderdata3=pd.DataFrame(data=zip(murdercities,murderstates,lat,long),columns=['Cities','States','Lat','Long'])      
#murderdata3.set_index('Cities',inplace=True)

#top10=list(murderdata1['City'].value_counts().keys())[:10]

#dadeindex=murderdata3[murderdata3['Cities']=='Dade'].index[0]
#murderdata3['Lat'][dadeindex]=28.3647
#murderdata3['Long'][dadeindex]=-82.1959

#bcindex=murderdata3[murderdata3['Cities']=='Baltimore city'].index
#bindex=murderdata3[murderdata3['Cities']=='Baltimore'].index
#murderdata3['Lat'][bcindex]=murderdata3['Lat'][bindex]
#murderdata3['Long'][bcindex]=murderdata3['Long'][bindex]

#murderdata3['Lat'].value_counts()
#murderdata3=murderdata3[murderdata3['Lat']!='?']
#murderdata3=murderdata3[murderdata3['Long']!='?']

#murderdata3.to_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\cleandatabase.csv',index=False)

""" END STEP 1 """

""" Step 2: Sorting Weapons Data 

The objective of this step is to clean the data and remove rows from the dataset where weapon used by perpetrator 
is not a gun. After doing this, we will add the co-ordinates from the new csv file we generated
Path: A:\\Ashish\\TestingProjects\\Datasets\\Homicide Reports (1980-2014)\\cleandatabase.csv
to the Homicide Reports dataset.

"""
weapons_df=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\database.csv',\
                        usecols=['Weapon','City','State'])
#murderdata1['Weapon'].value_counts()    
weapons_df['Lat']='?'
weapons_df['Long']='?'

weapons_df=weapons_df[weapons_df['Weapon']!='Knife']
weapons_df=weapons_df[weapons_df['Weapon']!='Blunt Object']
weapons_df=weapons_df[weapons_df['Weapon']!='Unknown']
weapons_df=weapons_df[weapons_df['Weapon']!='Explosives']
weapons_df=weapons_df[weapons_df['Weapon']!='Poison']
weapons_df=weapons_df[weapons_df['Weapon']!='Fall']
weapons_df=weapons_df[weapons_df['Weapon']!='Drugs']
weapons_df=weapons_df[weapons_df['Weapon']!='Drowning']
weapons_df=weapons_df[weapons_df['Weapon']!='Suffocation']
weapons_df=weapons_df[weapons_df['Weapon']!='Fire']
weapons_df=weapons_df[weapons_df['Weapon']!='Strangulation']

murderdata3=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\cleandatabase.csv')

for i in range(len(murderdata3['Cities'])):
    cityname=murderdata3['Cities'][i]
    indexi=weapons_df[weapons_df['City']==cityname].index
    if indexi.size!=0:
        weapons_df['Lat'][indexi[0]]=cityname=murderdata3['Lat'][i]
        weapons_df['Long'][indexi[0]]=cityname=murderdata3['Long'][i]

weapons_df=weapons_df[weapons_df['Lat']!='?']
weapons_df=weapons_df[weapons_df['Long']!='?']
""" STEP 2 ENDS """

"""STEP 3 Plotting of Data

This is the final step where we use the Basemap tool from the matplotlib toolkit to plot data.
Projection: Mercator
I have commented a few lines in this step, which can be used as well to change how your map looks after plotting.

"""    
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
x=list(weapons_df.Long)
y=list(weapons_df.Lat)

xs,ys=map1(x,y)

weapons_df['xmerc']=xs
weapons_df['ymerc']=ys

for j,i in weapons_df.iterrows():
    map1.plot(i.xmerc,i.ymerc,markerfacecolor='red',markeredgecolor='pink',marker='o',markersize=5,alpha=0.5)
   
plt.show()

"""STEP 3 ENDS"""