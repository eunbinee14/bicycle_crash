import pandas as pd
data= pd.read_csv('전처리후데이터.csv')

data.head()

data.info()
data.columns

# 필요한 열만 선택
# '사고일시', '피해차종' 제외
selected_columns=['사고등급', '가해자연령', '기상상태', '가해차종_개인형이동수단(PM)', '가해차종_건설기계', '가해차종_기타', '가해차종_농기계', '가해차종_불명',
                  '가해차종_사륜오토바이(ATV)', '가해차종_승용차', '가해차종_승합차', '가해차종_원동기장치자전거', '가해차종_이륜차',
      '가해차종_자전거', '가해차종_특수차', '가해차종_화물차', '가해자법규위반_과속', '가해자법규위반_교차로 통행방법 위반',
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


from sklearn.model_selection import train_test_split, cross_val_score

# 독립변수
X=data_subset.drop('사고등급', axis=1)
# 종속변수
y=data_subset['사고등급']
# 학습데이터 훈련데이터 설정
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.info()


# KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix

# KNN 생성
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 예측
y_pred = knn.predict(X_test)

# 정확도 평가
print(confusion_matrix(y_test, y_pred))
print('KNN 정확도:', end=' ')
print(metrics.accuracy_score(y_test, y_pred))

# cross validation of knn
acc_knn=cross_val_score(knn, X, y, cv=10)
print('KNN cv:', end=' ')
print(acc_knn.mean())


# Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# 특성 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 로지스틱 회귀 모델 생성
model_logist = LogisticRegression(max_iter=1000)
model_logist.fit(X_train, y_train)

# 정확도 계산1-model instance method
acuuracy1=model_logist.score(X_test, y_test)
print('로지스틱회귀 정확도1:', end=' ')
print(acuuracy1)

# 정확도 계산2-예측
from sklearn import metrics
from sklearn.metrics import confusion_matrix

y_pred = model_logist.predict(X_test)

accuracy2 = metrics.accuracy_score(y_test, y_pred)
print('로지스틱회귀 정확도2:', end=' ')
print(accuracy2)


# SVM
from sklearn import svm

# SVM 모델 생성1
model_svm = svm.SVC(kernel='rbf')
# 모델 학습
model_svm.fit(X_train, y_train)

# 예측
y_pred = model_svm.predict(X_test)

# 정확도 평가
print('SVM 정확도1:', end=' ')
print(metrics.accuracy_score(y_test, y_pred))


# SVM 모델 생성2
model_svm2 = svm.SVC(kernel='linear')
# 모델 학습
model_svm2.fit(X_train, y_train)

# 예측
y_pred = model_svm2.predict(X_test)

# 정확도 평가
print('SVM 정확도2:', end=' ')
print(metrics.accuracy_score(y_test, y_pred))