import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data = pd.read_csv('전처리후데이터.csv')

## 상관관계 분석 시각화 - heatmap ##
# 가해자법규위반 -> 500건 이상만 상관관계 분석에 이용
# Y : 사고등급

cols=['가해자성별','가해자연령','가해자신체상해정도','피해자성별','피해자연령','피해자신체상해정도','기상상태','사망자수','부상자수']

# '가해차종_원동기장치자전거','가해차종_자전거','피해차종_보행자','피해차종_원동기장치자전거','피해차종_자전거','가해자법규위반_기타','가해자법규위반_신호위반',
      # '가해자법규위반_안전운전 의무 불이행','가해자법규위반_안전운전불이행'
# #사고유형_차대사람 - 기타','사고유형_차대사람 - 길가장자리구역통행중','사고유형_차대사람 - 보도통행중',
# '사고유형_차대사람 - 차도통행중','사고유형_차대사람 - 횡단중','사고유형_차대차 - 기타','사고유형_차대차 - 정면충돌','사고유형_차대차 - 추돌',
# '사고유형_차대차 - 추돌 - 주정차중','사고유형_차대차 - 추돌 - 진행중','사고유형_차대차 - 측면직각충돌','사고유형_차대차 - 측면충돌',
# '사고유형_차대차 - 후진중충돌','사고유형_차량단독 - 공작물충돌','사고유형_차량단독 - 기타','사고유형_차량단독 - 도로외이탈 - 추락',
# '사고유형_차량단독 - 전도','사고유형_차량단독 - 전도전복','사고유형_차량단독 - 전도전복 - 전도'

# # pearson 상관관계 계산
corr = data[cols].corr(method = 'pearson')


#heatmap 그리기
fig = plt.figure(figsize = (12, 10))
ax = fig.gca()

# heatmap 안의 font-size 설정
sns.set(font_scale = 0.4)
heatmap = sns.heatmap(corr.values, annot = True, fmt='.2f', annot_kws={'size':14},
                      yticklabels = cols, xticklabels = cols, ax=ax, cmap = "coolwarm")

# X, Y 축 눈금 간격 조정
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(rotation=0, ha='right', fontsize=8)

plt.tight_layout()
plt.show()