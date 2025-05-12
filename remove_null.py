import pandas as pd

df=pd.read_csv('exercise_data.csv')

df.dropna(inplace=True)

print(df.to_string())
