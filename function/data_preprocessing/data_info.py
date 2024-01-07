import pandas as pd

# 2015-2020_사고.csv 데이터 파일 불러오기
df = pd.read_csv('2015-2020_사고.csv')

# 데이터의 기본 정보 확인
df.info()
