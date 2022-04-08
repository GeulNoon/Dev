from konlpy.tag import Kkma
import matplotlib.pyplot as plt
from collections import Counter
from gensim.models import Word2Vec
import random

word = ''
text1 = ''
with open('summary_sentences.txt',encoding = 'utf-8') as f:
    text1 = f.readlines()
    f.close()

text2 = ''
with open('topic_sentences.txt',encoding = 'cp949') as f:
    text2 = f.readlines()
    f.close()
                
kkma = Kkma()
w2v_noun = []
num = len(text1)
for i in range(0,num):
    w2v_noun.append(kkma.nouns(text1[i]))
    
num2 = len(text2)
for i in range(0,num2):
    if i not in w2v_noun : 
        w2v_noun.append(kkma.nouns(text2[i]))
        

def W2V(word):
    model = Word2Vec(sentences = w2v_noun, window = 5, min_count = 5,workers = 10, sg=0)
    example = model.wv.most_similar(word)
    
    word_list = []
    for i in range(len(example)):
        if len(example[i][0]) > 1 :
            word_list.append(example[i][0])
    
    w2v_word = []
    for i in range(4):
        if i not in w2v_word : 
            w2v_word.append(random.choice(word_list))
        
    return w2v_word
    