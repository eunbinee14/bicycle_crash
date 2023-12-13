import pandas as pd
data= pd.read_csv('전처리후데이터.csv')

data.head()

data.info()
data.columns

# 필요한 열만 선택
# '사고일시' 전처리 필요
selected_columns=['사고등급', '가해자연령', '기상상태', '가해차종_개인형이동수단(PM)', '가해차종_건설기계', '가해차종_기타', '가해차종_농기계', '가해차종_불명',
                  '가해차종_사륜오토바이(ATV)', '가해차종_승용차', '가해차종_승합차', '가해차종_원동기장치자전거', '가해차종_이륜차',
      '가해차종_자전거', '가해차종_특수차', '가해차종_화물차', '피해차종_개인형이동수단(PM)', '피해차종_건설기계', '가해자법규위반_과속', '가해자법규위반_교차로 통행방법 위반',
       '가해자법규위반_교차로운행방법위반', '가해자법규위반_기타', '가해자법규위반_미분류', '가해자법규위반_보행자 보호의무 위반',
       '가해자법규위반_보행자보호의무위반', '가해자법규위반_불법유턴', '가해자법규위반_신호위반', '가해자법규위반_안전거리 미확보',
       '가해자법규위반_안전거리미확보', '가해자법규위반_안전운전 의무 불이행', '가해자법규위반_안전운전불이행',
       '가해자법규위반_중앙선 침범', '가해자법규위반_중앙선침범', '가해자법규위반_직진우회전진행방해', '가해자법규위반_차로위반',
       '사고유형_차대사람 - 기타', '사고유형_차대사람 - 길가장자리구역통행중', '사고유형_차대사람 - 보도통행중',
       '사고유형_차대사람 - 차도통행중', '사고유형_차대사람 - 횡단중', '사고유형_차대차 - 기타',
       '사고유형_차대차 - 정면충돌', '사고유형_차대차 - 추돌', '사고유형_차대차 - 추돌 - 주정차중',
       '사고유형_차대차 - 추돌 - 진행중', '사고유형_차대차 - 측면직각충돌', '사고유형_차대차 - 측면충돌',
       '사고유형_차대차 - 후진중충돌', '사고유형_차량단독 - 공작물충돌', '사고유형_차량단독 - 기타',
       '사고유형_차량단독 - 도로외이탈 - 추락', '사고유형_차량단독 - 전도', '사고유형_차량단독 - 전도전복',
       '사고유형_차량단독 - 전도전복 - 전도']
data_subset = data[selected_columns]


from sklearn.model_selection import train_test_split

# 독립변수
X=data_subset.drop('사고등급', axis=1)
# 종속변수
y=data_subset['사고등급']
# 학습데이터 훈련데이터 설정
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.info()

# KNN모델
#model=
# 정확도 계산
#accuracy = model.score(X_test, y_test)
#print("모델 정확도: ", accuracy)

# 다중공산성
from statsmodels.stats import outliers_influence

vif = pd.DataFrame()
vif['features'] = X_train.columns
vif['VIF Factor'] = [outliers_influence.variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
vif.round(1)
