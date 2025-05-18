import pandas as pd

df=pd.read_csv('exercise_data.csv')

#Covnert 'Date' column to datetime, coercing errors
df['Date']=pd.to_datetime(df['Date'], errors='coerce', format='%Y /%m /%d')

print(df.to_string())