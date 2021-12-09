# Sentence-Transformer를 활용한 텍스트 유사도 측정
## 1. 직접 요약문과 KoBART/TextRank 생성 요약문의 텍스트 유사도 비교
최종 요약 모델 선정을 위해 7개의 지문 속 30개 문단을 직접 요약한 직접 요약문을 각각 KoBART 생성 요약문, TextRank 생성 요약문과 비교해 텍스트 유사도를 산출하였다. 그리고 마지막에 두 모델 과의 텍스트 유사도 평균을 구해 비교하였다.  
##### **실행 방법**: colab에서 문장별로 실행
##### 학습: klue/roberta-base 모델을 KLUE 내 STS 데이터셋을 활용하여 훈련하면 sentence-klue-roberta-base 모델을 도출할 수 있다. 

#### 필요한 데이터: test.csv
## 2. KoBART 생성 요약문과 사용자 요약문 간의 텍스트 유사도 비교
사용자 입력 요약문 채점을 하기 위해 Kobart summarization으로 생성한 요약문 모범답안과 사용자 요약문의 텍스트 유사도를 Sentence-Transformer를 이용해 구한다. 모델 학습은 위의 과정과 동일하다. Kobart summarization으로 미리 생성한 요약문과 사용자가 입력한 요약문의 텍스트 유사도를 비교하고 산출된 5개의 텍스트 유사도의 평균값에 100을 곱한 뒤 이를 사용자의 지문 이해도로 출력한다.
##### **실행 방법**: colab에서 문장별로 실행
##### 학습: klue/roberta-base 모델을 KLUE 내 STS 데이터셋을 활용하여 훈련하면 sentence-klue-roberta-base 모델을 도출할 수 있다. 

#### 필요한 데이터: test2.csv (2009년 수능 언어영역 지문)
###### [Sentence-Transformer를 활용한 텍스트 유사도 측정에 대한 자세한 블로그](https://viscachalog.tistory.com/entry/%EC%A1%B8%EC%97%85%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-Sentence-Transformers%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%9C%A0%EC%82%AC%EB%8F%84-%EC%B8%A1%EC%A0%95)

