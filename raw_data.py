import pandas as pd

raw_data=pd.read_csv('2015_2020.csv', encoding='cp949')

# 기존 캡스톤 때 진행했던 2015-2017년 데이터와 새로 생긴 2018-2020 데이터를 합치면서 데이터 값의 일관성이 꺠진 부분 발생
# 사고등급 열에 어떤 것은 중상사고로 입력 되어있고 어떤 것은 중상으로 입력되어있음
# 사고등급 열에 사고가 붙어 있는 경우를 제거
raw_data['사고등급'] = raw_data['사고등급'].str.replace('사고', '')
print(raw_data)

# 새로운 데이터 csv 파일로 형성
raw_data.to_csv('2015-2020_사고.csv', index=False)