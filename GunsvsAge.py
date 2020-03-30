# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:25:34 2020

@author: Ashish
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
weapons_df=pd.read_csv(r'A:\Ashish\TestingProjects\Datasets\Homicide Reports (1980-2014)\database.csv',\
                 usecols=['Perpetrator Age','Weapon'])

#Cleaning Data 
 
weapons_df=weapons_df[weapons_df['Perpetrator Age']!=' ']
weapons_df['Perpetrator Age']=weapons_df['Perpetrator Age'].astype('int32')
weapons_df['Perpetrator Age']=weapons_df[weapons_df['Perpetrator Age']>15]  
weapons_df['Perpetrator Age']=weapons_df[weapons_df['Perpetrator Age']<100]

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

weapons_df['PAgeGroup']='?'

weapons_df.index=np.arange(len(weapons_df['Weapon']))

indices=weapons_df[(weapons_df['Perpetrator Age']>15) & (weapons_df['Perpetrator Age']<20)].index
print(len(indices))
for i in indices:
    weapons_df['PAgeGroup'][i]='15-20'

indices=weapons_df[(weapons_df['Perpetrator Age']>=20) & (weapons_df['Perpetrator Age']<30)].index
for i in indices:
    weapons_df['PAgeGroup'][i]='20-30'

indices=weapons_df[(weapons_df['Perpetrator Age']>=30) & (weapons_df['Perpetrator Age']<40)].index
for i in indices:
    weapons_df['PAgeGroup'][i]='30-40'

indices=weapons_df[(weapons_df['Perpetrator Age']>=40) & (weapons_df['Perpetrator Age']<50)].index
for i in indices:
    weapons_df['PAgeGroup'][i]='40-50'

indices=weapons_df[(weapons_df['Perpetrator Age']>=50) & (weapons_df['Perpetrator Age']<60)].index
for i in indices:
    weapons_df['PAgeGroup'][i]='50-60'

indices=weapons_df[(weapons_df['Perpetrator Age']>=60) & (weapons_df['Perpetrator Age']<100)].index
for i in indices:
    weapons_df['PAgeGroup'][i]='60-100'


print("Done")
weapons_df.drop(columns=['Perpetrator Age'],inplace=True)

weapons_df=weapons_df[weapons_df['PAgeGroup']!='?']

ages=weapons_df['PAgeGroup'].value_counts().keys().tolist()
agescount=weapons_df['PAgeGroup'].value_counts().tolist()
df=pd.DataFrame(zip(ages,agescount),columns=['Age Groups','No. of cases'])
print('The Age Group highly associated with Gun Violence is: ',ages[0])

sns.barplot(x='Age Groups',y='No. of cases',data=df)
plt.show()

plt.pie(agescount,labels=ages,autopct='%1.0f%%', pctdistance=0.6, labeldistance=1.2)
plt.show()
