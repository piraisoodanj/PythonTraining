import pandas as pd

df1 ={"Name": ['Dhoni','40','jharkhand'],
         "Age": ['Hardik','30','Delhi'],
         "City": ['DUbe','32','Mumbai']}


df2 ={"Name": ['virat','35','Delhi'],
         "Age": ['KL','30','Mumbai'],
         "City": ['Rohit','33','Mumbai']}

df3 = pd.concat([df1,df2])