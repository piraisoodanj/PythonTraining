"""Data frame example"""

import pandas as pd

name = pd.Series(['Hardik','Virat'])
team = pd.Series(['MI','RCB'])

dic={'Name': name,'Team':team}
df= pd.DataFrame(dic)

print(df)