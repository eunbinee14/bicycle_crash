import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import seaborn as sns

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data = pd.read_csv('전처리후데이터.csv')

## 원핫인코딩으로 전처리한 데이터셋으로 카테고리(피해차종) 별로 사고 횟수가 얼만큼인지 시각적으로 파악 ##


# 각 카테고리별로 사고 횟수
count_by_vehicle_type = data.filter(like='피해차종').sum()

# bar 그래프로 시각화
plt.figure(figsize=(10, 5))
bars = plt.bar(count_by_vehicle_type.index, count_by_vehicle_type)

# X축 눈금 간격 조정 - 사이 간격
plt.xticks(rotation=45, ha='right')  # 레이블을 읽기 쉽게 회전
plt.xticks(range(len(count_by_vehicle_type)), count_by_vehicle_type.index)  # x-tick 위치 조정

# 막대 위에 카운트 값을 표시
for bar, count in zip(bars, count_by_vehicle_type):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() + 0.1, str(count), fontsize=9)

plt.title('피해차종별 사고 횟수')
plt.xlabel('피해차종')
plt.ylabel('사고 횟수')
plt.tight_layout()
plt.show()