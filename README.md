# bicycle_crash

## Topic : 한강변 충돌 사고로 인해 발생한 사고 등급 예측

### 1. 기존 진도 대비 추가 개발된 정도
캡스톤 디자인1 기존 진도 : 한강변의 높은 사고율 지역을 파악하고, 그 중에서 사고 다발 구역의 지형적 특성을 파악하기 위해 구글맵과 네이버지도를 모두 활용하였다. 
코드를 이용하여 실습을 진행하지 않고, 해당 지도를 이용하여 수기로 다양한 각도의 이미지를 수집하였고, 지형의 특징을 설명 및 정리하였다.

파이데 연계실습 개발 정도 : 새로 업데이트된 데이터셋을 활용하여 캡스톤 디자인1에서 가진 자동화에 대한 이슈를 해결하고자 주제 방향성을 바꾸었다. 
사고등급을 예측하는 것으로 주제를 변경하였고, 이에 맞춰 전처리를 진행하였다. 또한 데이터의 구성 및 흐름을 파악하기 위해 시각화와 다양한 분류 모델링을 진행하였다.

------------------------------------------------------------------------------------------------------------------------------------------


#### 전처리
- 캡스톤1에서는 2015-2017 도로교통공단 자전거 사고 다발지역 데이터와 2018-2020 데이터를 따로 수집하고, 병합하여 사용하였지만,
이번 파이데 캡스톤 연계실습에서는 2018-2020 데이터까지 한 번에 있는 데이터셋을 새로 수집하여 진행함
- 새로운 데이터 일부가 기존 데이터와 표현이 다르게 되어있어 통일시켜줌
  ( file name -> raw_data )

  ex) 사고등급 열에 어떤 것은 중상사고로 입력 되어있고 어떤 것은 중상으로 입력

- 전처리 과정에서 가해자성별,기상상태,사고등급,피해자신체상해정도,가해자신체상해정도는 매핑함
- 가해차종,피해차종,가해자법규위반,사고유형에 대해서는 원-핫 인코딩적용
  ( file name -> preprocessing )

#### 시각화
##### 여러 시각화를 진행하여 데이터셋의 추세 및 구성 파악
- 변수간의 상관관계 분석 시각화 ( file name -> correlaton_matrix )
- 사고등급에 따른 피해자, 가해자 각자 신체상해정도가 얼마나 되는지 평균 막대 그래프 시각화( file name -> accident_grade )
- 사고 시간대별 사고 발생 횟수 시각화 ( file name -> visual_accident_time )
- 원-핫인코딩으로 전처리한 데이터셋으로 카테고리(피해차종, 가해차종, 가해자법규위반, 사고유형) 별로 사고 횟수가 얼만큼인지 시각화 ( file name -> visual_damage_car, visual_inflict_car, visual_inflict_violation, visual_accident_type ) 

#### 모델링
- 종속변수를 '사고등급', 독립변수를 '사고등급' 제외하고 모두 포함하여 classification
- train, test 데이터 설정
- KNN 모델을 활용하여 정확도 평가, cross validation으로 반복 평가
- Logistic regression 모델 생성하여 정확도 평가
  - 로지스틱 모델 인스턴스 메소드로 평가
  - accuracy_score로 평가
- SVM 모델 생성하여 정확도 평가
  - 커널 함수 rbf로 설정
  - 커널 함수 linear로 설정
