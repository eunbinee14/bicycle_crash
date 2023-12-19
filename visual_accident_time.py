import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('전처리후데이터.csv')

## 사고 시간대별 사고 발생 횟수 ##

# '사고일시' 칼럼을 datetime 형식으로 변형
data['사고일시'] = pd.to_datetime(data['사고일시'])

# 시간대별 사고 개수 계산
accident_count = data.groupby(data['사고일시'].dt.strftime('%H:%M:%S')).size().reset_index(name='accident_count')

print(accident_count)

# 시간대별 사고 횟수 플랏
plt.figure(figsize=(30, 8))
plt.plot(accident_count['사고일시'], accident_count['accident_count'], marker='o', linestyle='-', color='b')
plt.title("number of accidents by Time ")
plt.xlabel("time")
plt.ylabel("accident_count")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()