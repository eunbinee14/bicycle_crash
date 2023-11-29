import pandas as pd
df = pd.read_csv('2015-2020_사고.csv')

# 피해자 성별에 '기타불병'과'없음'이 존재
# '없음'을 '기타불명'으로 바꾸기
df['피해자성별'] = df['피해자성별'].replace('없음', '기타불명')

# 가해자성별을 수치형으로 매핑(남->0, 여->1, 기타불명 ->2)
gender_mapping1 = {'여': 0, '남': 1, '기타불명': 2}
df['가해자성별'] = df['가해자성별'].map(gender_mapping1)
# 피해자성별을 수치형으로 매핑(남->0, 여->1, 기타불명 ->2)
gender_mapping2 = {'여': 0, '남': 1, '기타불명': 2}
df['피해자성별'] = df['피해자성별'].map(gender_mapping2)

# '사고일시' 열과 '사고시간대' 열을 datetime 형태로 변환
df['사고일시'] = pd.to_datetime(df['사고일시'])
df['사고시간대'] = pd.to_timedelta(df['사고시간대'] + ':00:00')  # add ':00:00' to ensure the correct format
df['사고일시'] = df['사고일시'] + df['사고시간대']

# '사고시간대' 열은 더 이상 필요하지 않으니 삭제
df = df.drop(columns=['사고시간대'])

# 연령에 있는 '불명'을 NaN으로 대체하고 연령에 대해 '세' 제거하고 숫자로 변환
df['가해자연령'] = pd.to_numeric(df['가해자연령'].replace('불명', float('nan')).str.replace('세', ''), errors='coerce')
df['피해자연령'] = pd.to_numeric(df['피해자연령'].replace('불명', float('nan')).str.replace('세', ''), errors='coerce')

# 연령 결측치를 각각의 열의 평균값으로 대체
mean_age_gahaeja = df['가해자연령'].mean()
mean_age_pihaeja = df['피해자연령'].mean()

df['가해자연령'] = df['가해자연령'].fillna(mean_age_gahaeja)
df['피해자연령'] = df['피해자연령'].fillna(mean_age_pihaeja)

# 매핑하기 위해 '기상상태' column에 어떤 데이터가 있는지 확인
unique_weather_states = df['기상상태'].unique()
print(unique_weather_states)

# '기상상태'를 날씨별로 매핑
weather_mapping = {'맑음': 0, '흐림': 1, '비': 2, '기타/불명': 3, '기타': 3,'눈':4,'안개':5}
df['기상상태'] = df['기상상태'].map(weather_mapping)

# 매핑하기 위해 '사고등급'.'피해자신체상해정도','가해자신체상해정도' column에 어떤 데이터가 있는지 확인
grade_states = df['사고등급'].unique()
print(grade_states)
harm_states1 = df['피해자신체상해정도'].unique()
print(harm_states1)
harm_states2 = df['가해자신체상해정도'].unique()
print(harm_states2)

# '사고등급','피해자신체상해정도','가해자신체상해정도' 매핑
grade_mapping = {'경상': 0, '중상': 1, '부상신고': 2,'사망':3}
df['사고등급'] = df['사고등급'].map(grade_mapping)
harm_mapping1={'경상': 0, '중상': 1, '부상신고': 2,'사망':3,'상해없음':4,'기타불명':5,'없음':6}
df['피해자신체상해정도']= df['피해자신체상해정도'].map(harm_mapping1)
harm_mapping2={'경상': 0, '중상': 1, '부상신고': 2,'사망':3,'상해없음':4,'기타불명':5}
df['가해자신체상해정도']=df['가해자신체상해정도'].map(harm_mapping2)

# '가해차종','피해차종,'가해자법규위반','사고유형'에 대해 원-핫 인코딩 적용
df_encoded = pd.get_dummies(df, columns=['가해차종', '피해차종','가해자법규위반','사고유형'], prefix=['가해차종', '피해차종','가해자법규위반','사고유형'])

# 결과 출력
print(df_encoded)