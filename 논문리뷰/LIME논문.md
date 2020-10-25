## LIME 논문 정리 (정리중)

## Paper
["Why Should I Trust You?": Explaining the Predictions of Any Classifier]( https://arxiv.org/abs/1602.04938)    

## Giuthub
[github 코드](https://github.com/marcotcr/lime)    

## Youtube
[유튜브 설명](https://youtu.be/hUnRCxnydCc)    

## LIME
1. 배경 – 기존 trust 의미와 확보방법 및 한계    
① trusting a prediction   
② trusting a model   
-> 기존의 trust 확보 방법: evaluate using accuracy metrics on an available validation dataset    
-> 기존 방법의 문제: real world data는 다를 수 있다는 문제 등    
=> inspect individual predictions and their explanations = LIME    

2. LIME 모델 정의/특징/알고리즘    
1) 정의    
-explanational model 중 하나로, uncertainty를 줄임과 동시에 human interpretable 하도록 complexity를 줄인다. 주어진 instance에 대강 local한 위치에서 model의 decision function을 예측할 수 있는 interpretable model을 찾는 것이 목적    
-algorithm that explain predictions of any classifier or regressor, by approximating it locally with an interpretable model    

2) 특징    
① interpretable: input variable과 예측 결과 사이의 관계를 설명할 수 있어야 함    
② local fidelity: 모델 전체가 아니라, 하나의 instance에 대해 왜 그렇게 움직이는지 설명할 수 있어야 함     
③ model-agnostic: 어떤 모델이든 적용 가능    
④ global perspective: 각각의 테스트 결과 말고도, 모델 전체가 왜 이런 경향성으로 움직이는지에 대한 global perspective도 가져야 모델에 대한 trust를 가질 수 있음    
 

3) 알고리즘    
\xi(x)\ =\ {argmin}_{g\inG}\ L(f,\ g,\pi_x)\ +Ω(g)     
 

**수식 용어 설명    
f(x): 평가하려고 하는 모델 f가 x를 넣었을 때 원하는 label에 대한 확률로 내놓는 값     
G: class of (potentially) interpretable models (e.g. Linear model, Decision Tree)    
g: d’ dimension의 {0, 1} vector. Interpretable component가 있는지, 없는지     
Ω(g): explainer model의 complexity (e.g. decision tree의 depth, linear model의 number of non-zero wights)     
\pi_x : input x와 sample instance z 간의 가까운 정도의 measure    
L(f,\ g,\pi_x) : 정의된 pi와 주어진 f에 대해, g가 주어진 f를 approximate 하는 데에 대한 uncertainty (주어진 sample instance z 근처에서)    
  
**주의: 실제 모델에서 사용하는 feature (e.g. word embedding)과 interpretable data representation (e.g. one-hot word vector)는 다름    

**파이썬 패키지: lime    

## SP(Submodular Pick) LIME   
1. 정의 및 특징    
- method that selects a set of representative instances with explanations to address the trusting the model problem via submodular optimization    
-LIME은 한 instance의 explanation을 설명할 수 있지만, model의 trust는 말할 수 없음    
-B개의 budget limit을 골라놓고, 중요한 feature들이 골라지도록 B 가지 미만의 test instnace를 고르는 문제임.    
-weighted pick cover (NP-HARD)라서 greedy하게 제일 목표함수값이 높아지는 instance를 선택해 나감   
-사용자는 B개의 instance 섦여 결과를 보고 이 model의 행동방식 유추 가능   

2. 알고리즘    
   

## 활용가능성   
### 수치 데이터에 lime 모델 적용한 결과    
 

### LIME 장단점     
1) (장점) 어떤 블랙박스 모델이든 사람이 이해할 수 있는 수준으로 설명 가능. 내부 동작 방식을 설명할 수 있다는 점에서 실무에서 활용 가능할 듯.     
2) (단점) 결과값을 가지고 거꾸로 유추하는 방식이므로 추가 학습이 필요하고, 속도 느림(e.g. Inception Net의 한 instance를 설명하는 데 10분이 걸린다고 함)    
3) (단점) input <-> interpretable feature의 가역적인 변환이 가능한 경우에만 사용할 수 있음     
 
### Grad Cam과의 차이    
-공통점: 입력이 주어졌을 때 모델 행동 분석하는 기법    
-차이점: Grad CAM (Gradient-weighted Class Activation Mapping, arxiv )은 CNN 모형에 적용할 수 있는 모형 해석 방법론. CNN 층(마지막)에 들어가는 그래디언트를 가지고 자료의 어느 부분에 가중치를 주는지 계산하는 방법. Global average pooling이라는 레이어를 가진 특수한 CNN 구조에서만 사용 가능하고, 기울기 정보 없이 순전파 때 액티베이션 값을 활용    

## 참고문헌
[Why Should I Trust You? Explaining the Predictions of Any Classifier 논문 정리](http://shuuki4.github.io/deep%20learning/2016/08/24/Why-Should-I-Trust-You-%EB%85%BC%EB%AC%B8-%EC%A0%95%EB%A6%AC.html)    
https://dreamgonfly.github.io/blog/lime/    

