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

def func_test(val):
    return val['Age'] / val['Work_Exp']

#axis=1 is row wise 
dt4['is even']=dt4['Work_Exp'].apply(func_test,axis=1)
print(df)