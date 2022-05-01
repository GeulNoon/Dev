from konlpy.tag import Kkma
import matplotlib.pyplot as plt
from collections import Counter
from gensim.models import Word2Vec
import random

def W2V(word):

    ko_model = Word2Vec.load("././ko/ko.bin")#디렉토리 수정
    example = ko_model.wv.most_similar(word)
    
    word_list = []
    for i in range(len(example)):
        if len(example[i][0]) > 1 :
            word_list.append(example[i][0])
    
    w2v_word = []
    for i in range(4):
        if i not in w2v_word : 
            w2v_word.append(random.choice(word_list))
    
        
    return w2v_word


