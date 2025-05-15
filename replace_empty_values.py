import pandas as pd

df=pd.read_csv('exercise_data.csv')

df.fillna(130, inplace=True)