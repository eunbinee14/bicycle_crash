import pandas as pd

# 도로교통공단_자전거사고 다발지역 개별사고 정보_20171231.csv 데이터 파일 불러오기
df = pd.read_csv('도로교통공단_자전거사고 다발지역 개별사고 정보_20171231.csv',encoding="ANSI")


print(df)
