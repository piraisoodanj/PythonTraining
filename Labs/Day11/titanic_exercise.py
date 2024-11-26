import pandas as pd


df=pd.read_csv(r"C:\Users\Administrator\Desktop\UST_Training\Titanic\titanic.csv")

#compare the average age of passengers who survived with those who didn't
# Avg_age_Survivied = df[df['Survived']==1]['Age'].mean()
# print(Avg_age_Survivied)
# Avg_age_notSurvivied = df[df['Survived']==0]['Age'].mean()
# print(Avg_age_notSurvivied)


#calculate the survival rate by gender
# print(df.groupby('Sex')['Survived'].mean())

df['Family_Size']=df['SibSp'] + df['Parch']
#print(df[['SibSp','Parch','Family_Size']].head(2))
family_survived= df.groupby('Family_Size')['Survived'].mean().reset_index()
family_survived.columns = ['Family_Size','Family_Survival_Rate']
print(family_survived)

df=pd.merge(df,family_survived,on='Family_Size',how='left')
print(df[['Family_Size','Family_Survival_Rate']].head(10))

