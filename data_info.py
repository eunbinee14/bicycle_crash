import pandas as pd


df = pd.read_csv('도로교통공단_자전거사고 다발지역 개별사고 정보_20171231.csv',encoding="ANSI")

# 데이터의 기본 정보 확인
df.info()
