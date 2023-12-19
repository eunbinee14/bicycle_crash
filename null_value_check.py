import pandas as pd
# 2015-2020_사고.csv 파일 불러오기
df = pd.read_csv('2015-2020_사고.csv')

# null값 확인
print(df.isnull().sum())
