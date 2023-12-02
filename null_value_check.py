import pandas as pd

df = pd.read_csv('2015-2020_사고.csv')

# null값 확인
print(df.isnull().sum())
