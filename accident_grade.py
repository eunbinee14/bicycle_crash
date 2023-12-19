import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data = pd.read_csv('전처리후데이터.csv')

## 사고등급에 따른 피해자, 가해자 각각 신체상해정도가 얼머나 되는지 평균 막대 그래프 시각화 ##


# 사고등급에 따른 가해자 신체상해정도의 평균 계산
average_injury_by_grade = data.groupby('사고등급')['가해자신체상해정도'].mean().reset_index()

# 가해자 신체상해정도에 대한 bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='사고등급', y='가해자신체상해정도', data=average_injury_by_grade, palette='viridis')
plt.title('사고등급에 따른 평균 가해자 신체상해정도')
plt.xlabel('사고등급')
plt.ylabel('평균 가해자 신체상해정도')
plt.show()

# 사고등급에 따른 피해자 신체상해정도의 평균 계산
average_injury_by_grade = data.groupby('사고등급')['피해자신체상해정도'].mean().reset_index()

# 가해자 신체상해정도에 대한 bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='사고등급', y='피해자신체상해정도', data=average_injury_by_grade, palette='viridis')
plt.title('사고등급에 따른 평균 피해자 신체상해정도')
plt.xlabel('사고등급')
plt.ylabel('평균 피해자 신체상해정도')
plt.show()
