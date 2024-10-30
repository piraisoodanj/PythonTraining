"""Iter rows"""

import pandas as pd

dictio ={"Name": ['Dhoni','Hardik'],
         "Team": ['CSK','MI']}


df = pd.DataFrame(dictio,index=['RANK 1','RANK 2'])
#print(df)


for row_index,row_value in df.iterrows():
    print('--------------')
    print("row_index is:",row_index)
    print("row_value is:", row_value)

    