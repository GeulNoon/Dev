KoNLPy를 이용한 형태소 분석

문제를 출제하기 위해서는 지문의 문장과 단어를 토큰화하는 자연어 처리 과정이 필수적이다.
파이썬으로 자연어 처리를 하는 경우 KSS(Korean Sentence Splitter)로 문장 토큰화를 할 수 있으며 KoNLPy의 형태소 분석기를 사용할 수 있다.
KoNLPy에는 Okt(Open Korea Text), 꼬꼬마(Kkma), 한나눔(Hannanum), 코모란(Komoran), 메캅(Mecab)이 있으며 각 분석기로 같은 문장을 토큰화해보았다.

<요구사항>
1. KoNLPy 설치: pip install konlpy
2. JPype 1.2.0 cp38 설치
3. KSS 설치: pip install kss
4. anaconda3(Python 3.8) 설치
5. JDK 16.0.1 설치

<형태소 분석 시 공통적으로 활용할 메소드 종류>
1) morphs : 형태소 추출
2) pos : 품사 태깅(Part-of-speech tagging)
3) nouns : 명사 추출
