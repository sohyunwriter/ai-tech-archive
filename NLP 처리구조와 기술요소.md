# NLP 처리구조와 기술요소       
Assembled by Sohyeon Yim (2020-06-13)   

## NLP 처리 구조    
![nlp 처리구조](https://user-images.githubusercontent.com/44013936/84567468-cb502580-adb3-11ea-9c03-b7e40cc908e3.png)
* 사용자가 발화를 하면 해당 발화를 인식해 text로 변환한다. (Speech-to-Text, Speech Recognition)   
* text의 형태소, 구문 분석 뿐만 아니라, 의미를 인식한다. (Natural Language Understanding)   
* 대화 흐름과 상황을 고려해서 사용자의 발화의 의도에 대한 최선의 대화 전략을 결정해 다음 발화에 해당하는 의미 표현을 생성한다. 이때, 기존의 rule-based 방식이 있고, 머신 러닝 방식이 있다. (Diaglog Management)   
* 기계적 표현을 자연어 기반 문장으로 생성한다. (Natural Language Generation)      
* 해당 텍스트를 자연어 음파로 변환한다. (Text-to-Speech, Speech Synthesis)   

## NLP 기술 요소   

### 음성 변환   
1. STT (Speech-to-Text, Speech Recognition)   
* 4KHz 음성신호를 문자(Text)로 변환   
* 가우시안 필터, 특징추출, 디코더   

2. TTS (Text-to-Speech, Speech Synthesis)   
* 문자(Text)를 자연어 음파로 변환   
* 분절음 diphone, 텍스트 음소 변환   

### 언어 처리   
1. NLU (Natural Language Understanding)   
* 자연어 어휘/문장/문맥 패턴기반 이해   
* 형태소/구문 분석, Word Embedding, Word2Vec   

2. NLG (Natural Language Generation)   
* 기계적 표현을 자연어 기반 문장 생성   
* 자연어 표현생성, 후보 문장 비교/선택   

### 대화 관리(Diaglog Management)   
1. 머신 러닝 대화 관리   
* 통계와 패턴 기반 대화 관리   
* RNN, LSTM, Seq2Seq   

2. 규칙 기반 대화 관리   
* 규칙 기반 정확성 높으나 범용성 저하   
* 개별 규칙 생성, 대화 DB, Syllabus   

## Reference & Additional Resources   
[자연어처리, NLP](http://blog.skby.net/%EC%9E%90%EC%97%B0%EC%96%B4%EC%B2%98%EB%A6%ACnlp-natural-language-processing/)   
[인간의 언어를 이해하는 기계, NLU](https://blog.lgcns.com/1672)    
