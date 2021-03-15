## Machine-Learning
Python을 통한 Machine Learning
#### AI(Aritificial intelligence)
: 인간 학습하고 생각하는 능력을 컴퓨터로 구현하는 것. 가장 포괄적인 상위 개념. 


< 기계학습(ML : Machine Learning) > <br>


: AI를 구현하는 방법의 하나. <br> : 애플리케이션을 수정하지 않고도 주어진 데이터를 기반으로 패턴을 학습. <br> : 학습을 바탕으로 미래값을 예측하는 기술.


- 지도학습(Supervised Learning)
  - 회귀(Regression)
  - 분류(Classification)
  - 감지/인지
  - 추천
  - 분석

    - 대표적인 알고리즘
      - K-최근접 이웃(K-nearest neighbors)
      - 선형회귀(Linear regression)
      - 로지스틱 회귀(Logistic regression)
      - 서포트 벡터 머신(SVM: Support vector machines)
      - 결정 트리(Decision tree)와 랜덤 포레스트(random forest)
      - 신경망(Neural Network)

<br>

- 비지도 학습(Unsuperbised Learning)
  - 군집화(Clustering)
    - K-mean
    - DBSCAN
    - 이상치 탐지(outlier detection)과 특이치 탐지(novelty detection) 

  - 시각화(Visualization)와 차원축소(Dimensional reduction)
    - 주성분 분석(PCA : Principal component analysis)

<br>

- 강화 학습(Reinforcement learning)

<br>


  < 딥러닝(Deep Learning) >
  : 복잡한 형태의 신경망.
  - CNN(Convolutional Neural Networks)
  - RNN(Recurrent Neural Network) ex) LSTM
  - GAN(Generative Adversarial Networks)
  - Auto Encoder

#### 학습

- 학습의 목표 : 분류, 예측, 추천 등을 위한 모델( 기준식, 수학식, 수학 모델 ) 획득.
- 학습하기 : 적합할 것 같은 수학 모형을 설정하고 이 수학모형에 대한 Best 계수들을 찾는 것.


#### 텐서플로우(TensorFlow)

- http://www.tensorflow.org/?hl=ko
- 기계학습을 위한 오픈 소스 플랫폼.
- 기계학습 모델을 개발하고 학습시키는데 도움이 되는 핵심.


#### 파이썬 기계학습 생태계의 주요 패키지(Package)

- 기계학습 패키지
  - 사이킷런(Scikit-learn) -> 대표적인 기계학습 패키지.
  - 텐서플로우(TensorFlow), 케라스(Keras) -> 영상, 음성, 언어 등의 비정형 데이터 분야에서의 딥러닝에 특화.

- 행렬/ 선형대수/ 통계패키지
  - 넘파이(Numpy) -> 행렬 기반 데이터 처리에 특화.

- 데이터 핸들링 패키지
  - 판다스(Pandas) -> 2차원 데이터 처리에 특화.

- 시각화 패키지
  - 맷플롯립(Matplotlib)
  - 시본(Seaborn)

