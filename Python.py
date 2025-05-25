import pandas as pd
df=pd.DataFrame()
print(df)
columns=['A','B','V']
width=[1,2,3,4]
df=df[columns]
print(df)
df1=df.copy()
column1=columns[::-1]
df2=df1.copy()
df2=df2[column1]