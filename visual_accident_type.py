import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import seaborn as sns

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data = pd.read_csv('전처리후데이터.csv')

## 원핫인코딩으로 전처리한 데이터셋으로 카테고리(사고유형) 별로 사고 횟수가 얼만큼인지 시각적으로 파악 ##


# 각 카테고리별로 사고 횟수
count_by_vehicle_type = data.filter(like='사고유형').sum()

# bar 그래프로 시각화
plt.figure(figsize=(10, 5))
plt.bar(count_by_vehicle_type.index, count_by_vehicle_type)

# X축 눈금 간격 조정 - 사이 간격
plt.xticks(rotation=45)
plt.xticks(range(0, len(count_by_vehicle_type), 2), count_by_vehicle_type.index[::2])

plt.title('사고유형별 사고 횟수')
plt.xlabel('사고유형')
plt.ylabel('사고 횟수')
plt.tight_layout()
plt.show()
