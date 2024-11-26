import pandas as pd



dt1=pd.DataFrame({"Name":['Gayathri','SSS'],
    "Age":[30,54],
    "city":['chennai','Delhi']
    })


dt2=pd.DataFrame({"Name":['EEE','YYY'],
    "Age":[20,44],
    "city":['Kerala','Mumbai']})

#concat
dt3=pd.concat([dt1,dt2],ignore_index=True)
print(dt3)


#changing city name
# dt3.loc[2,'city']='Hyderabad'
# print(dt3)

#changing the value using loc
# dt3.loc[dt3['Name']=='EEE','city']='Kerala'
# print(dt3)


#NUll value
import numpy as np
dt3.loc[dt3['Name']=='SSS','city']=''
dt3.loc[dt3['Name']=='EEE','city']=np.nan

print(dt3)
#assign values for nan
dt3.fillna('NYC',inplace=True)
print(dt3)
#value counts
dt3['city'].value_counts()

