import pandas as pd


df=pd.read_csv(r"C:\Users\Administrator\Desktop\UST_Training\Titanic\titanic.csv")
#head function
#df.loc[:,'Age'].head(5)
#df['Age'].head()
#df1=df['Age']
#print(df1.head())

#two columns
# df1=df[['Age','Sex']]
# print(df1.head())

#age <25
# df1=df[df['Age']<25]
# print(df1)


#length of dataframe
#print(len(df.index))

#avg of age
#print(df['Age'].mean())

#avg fare price of all male  passenger whose age is <25
# df1=df[df['Age']<25]
# df1=df1[df1['Sex']=='male']
# df1=df1['Fare'].mean()
# print(df1)

df1=df[(df['Age']<25) & (df['Sex']=='male')]
df1=df1['Fare'].mean()
df1.to_csv("valfilt.csv",index=False)
#print(df1)


#percentage of passengers survived the titanic
# df_survive=df[df['Survived']==1]
# df_total=len(df.index)
# df=(df_survive/df_total *100)
# print(df)