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
print(dt4)

import numpy as np
#filing NAN value to some value
dt4.loc[dt4['Name']=='dhoni','city']='USA'
print(dt4)

#avg values
dt4.loc[dt4['Name']=='dhoni','Work_Exp']=dt4['Work_Exp'].mean()
print(dt4)


dt4.to_csv('test_output.csv',index=False)