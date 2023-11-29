import pandas as pd
df = pd.read_csv('2015-2020_사고.csv')

# 가해자성별을 수치형으로 변환 (예: 남->0, 여->1)
df['가해자성별'] = df['가해자성별'].map({'남': 0, '여': 1})

# 데이터 타입이 object인 사고일시를 datetime으로 변환
df['사고일시'] = pd.to_datetime(df['사고일시'])

print(df)
print(0)
