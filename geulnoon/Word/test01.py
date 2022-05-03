from .exam_func import TEST, MEAN,EXAMPLE, EXAMPLE_test
import json
from collections import OrderedDict
from .W2V_word import W2V

# 콤마, 괄호 삭제
def REMOVE(st):
    row = st
    row2 = ' '.join(s for s in row)
    remove = "'}"
    for x in range(len(remove)):
        row3 = row2.replace(remove[x],"")
    row4 = row3.replace("'","")
    return row4


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

#exam_word에서 뽑아온 1번문제 어휘
def t01(word):
    #W2V_word에서 뽑아온 보기 어휘
    w2v_word = W2V(word)

    #parsing에서 코드 추출
    t = TEST(word)
    result_parse = t[0]
    result_example = t[1]

    # 뜻 추출
    ex_mean = MEAN(result_parse)
    # 용례 추출
    ex_example = EXAMPLE(result_example)
    # 빈칸 문제 생성
    ex_test = EXAMPLE_test(ex_example, word)#5.01 수정

    mean = REMOVE(ex_mean)
    test = REMOVE(ex_test)


    w2v_mean = W2V_MEAN(w2v_word)
    
    choice = { name:value for name, value in zip(w2v_word, w2v_mean) }
    choice[word] = mean


    #json파일
    #문제 1번은 TEST1이 문제, 정답은 WORD, 해설은 MEAN
    file_exam1 = OrderedDict()
    file_exam1["TYPE1"] = "다음 단어 중 빈칸에 들어갈 수 있는 단어를 고르시오."
    file_exam1["TEST1"] = test   #문제
    file_exam1["ANSWER"] = word    #단어
    #file_exam1["MEAN"] = mean    #뜻
    #file_exam1["W2VWORD"] = w2v_word    #보기 단어
    #file_exam1["W2VMEAN"] = w2v_mean    #보기 단어 뜻
    file_exam1["CHOICE"] = choice
    #json파일
    EXAM1 = json.dumps(file_exam1, ensure_ascii=False, indent="\t")
    return EXAM1
