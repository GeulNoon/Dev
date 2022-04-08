from exam_word import word_03
from exam_func import TEST, MEAN,EXAMPLE, EXAMPLE_test
import json
from collections import OrderedDict
from W2V_word import W2V

#exam_word에서 뽑아온 3번문제 어휘
word = word_03
#W2V_word에서 뽑아온 보기 어휘
w2v_word = W2V(word)

#parsing에서 코드 추출
t = TEST(word)
result_parse = t[0]
result_example = t[1]

# 뜻 추출
ex_mean = MEAN(result_parse)

# 콤마, 괄호 삭제
def REMOVE(st):
    row = st
    row2 = ' '.join(s for s in row)
    remove = "'}"
    for x in range(len(remove)):
        row3 = row2.replace(remove[x],"")
    row4 = row3.replace("'","")
    return row4

mean = REMOVE(ex_mean)

#W2V 어휘들 뜻
def W2V_MEAN(w2v_word):
    n = len(w2v_word)
    w2v_mean = []
    for i in range(0,n):
        t = TEST(w2v_word[i])
        result_parse = t[0]
        row1 = MEAN(result_parse)
        row2 = REMOVE(row1)
        w2v_mean.append(row2)
    
    return w2v_mean

w2v_mean = W2V_MEAN(w2v_word)

#json파일
#문제 3번은 MEAN 문제, WORD 정답
file_exam3 = OrderedDict()
file_exam3["TYPE3"] = "다음 단어 중 주어진 사전적 의미에 부합하는 단어를 고르시오."
file_exam3["WORD"] = word    #단어
file_exam3["MEAN"] = mean    #뜻
file_exam3["W2VWORD"] = w2v_word    #보기 단어
file_exam3["W2VMEAN"] = w2v_mean    #보기 단어 뜻

#json파일
EXAM3 = json.dumps(file_exam3, ensure_ascii=False, indent="\t")