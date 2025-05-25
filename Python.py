import pandas as pd
df=pd.DataFrame()
print(df)
columns=['A','B','V']
column1=columns[::-1]
width=[1,2,3,4]
df=df[columns]
print(df)
df1=df.copy()
df2=df1.copy()
df2=df2[column1]