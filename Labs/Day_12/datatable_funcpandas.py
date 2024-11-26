import pandas as pd

dt1=pd.DataFrame({"Name":['Gayathri','SSS','dhoni','YYY'],
    "Age":[30,54,56,27],
    "Birth_city":['chennai','Delhi','NY','SG']
    })


dt2=pd.DataFrame({"Name":['Gayathri','SSS','YYY'],
    "Work_Exp":[20,44,67],
    "city":['Kerala','Mumbai','USA']})

#dt1 values comes using left and outer
dt4=pd.merge(dt1,dt2,on='Name',how='left')
#print(dt4)

import numpy as np
#filing NAN value to some value
dt4.loc[dt4['Name']=='dhoni','city']='USA'
#print(dt4)

# def me_function(val):
#     return val + 'city'

#dt4['city']=dt4['city'].apply(me_function)

 #nre column name is "is even" and teh value" if  work exp is even number or not, it should be boolean
 #method 1
# dt4['IS even']=dt4['Work_Exp']%2==0
# print(dt4)

#method 2
def func_test(val):
    return val%2==0

#method 3

#def func_test(val):

    # if(val%2==0):
    #     return True
    # else:
    #     return False

dt4['is even']=dt4['Work_Exp'].apply(func_test)
print(dt4)