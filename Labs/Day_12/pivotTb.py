import pandas as pd

data={
        'Store':['store1','store1','store2','store2','store3','store3','store4','store5'],
        'Region':['North','North','South','South','East','East','North','South'],
        'Sales':[200,150,300,250,400,350,100,200]
        }


df=pd.DataFrame(data)

#totalsales per store
#df1=df.groupby('Store').sum()
#print(df1)


#Method 1
#totalsales per Region
# df2=df.groupby('Region').sum().reset_index()
# print(df2)

# #merge orginal and region dt
# df3=pd.merge(df,df2,on='Region',how='left',suffixes=("_store","_region"))
# print(df3)

#Method2
regional_sales=df.groupby(['Region']).agg({'Sales':'sum'}).reset_index()

sales_aggregated_df=df.groupby(['Store','Region']).agg({'Sales':'sum'}).reset_index()
#print(sales_aggregated_df)

merged_Df=pd.merge(sales_aggregated_df,regional_sales,on='Region',how='left',suffixes=("_store","_region"))
merged_Df['SalesbyRegion%']=merged_Df['Sales_store']/merged_Df['Sales_region'] * 100
#print(merged_Df)

df=pd.merge(df,merged_Df,left_on=['Store','Region'],right_on=['Store','Region'],how='left')

print(df)