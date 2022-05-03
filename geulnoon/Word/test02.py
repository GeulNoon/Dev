# -*- coding: utf-8 -*-
from .exam_func import TEST, MEAN,EXAMPLE
import json
from collections import OrderedDict
from konlpy.tag import Kkma

def t02(word, temp):

    #parsing에서 코드 추출
    t = TEST(word)
    result_parse = t[0]
    result_example = t[1]

    # 뜻 추출
    ex_mean = MEAN(result_parse)
    # 용례 추출
    ex_example = EXAMPLE(result_example)

    # 콤마, 괄호 삭제
    def REMOVE(st):
        row = ' '.join(s for s in st)
        remove = "}"
        for x in range(len(remove)):
            row1 = row.replace(remove[x],"")
        row2 = row1.replace("'","")
        row3 = row2.split('.')
        strip_li = []
        for i in row3:
            i = i.strip()
            strip_li.append(i)
            
        return strip_li

    # 출제 어휘가 있는 문장과 문장 전후 추출
    def Sentence(st):
        sentence_list = []
        for i in range(len(st)):
            if word in st[i]:
                if(len(sentence_list) > 3):
                    break
                sentence_list.append(st[i-1])
                sentence_list.append(st[i])
                sentence_list.append(st[i+1])
        return sentence_list  
        
    # 뜻
    mean = REMOVE(ex_mean)
    # 용례
    example = REMOVE(ex_example)
    #5.03 추가 보기 문제 해결("또는"이 있을 때 문장이 두개로 나누어짐)
    for i in mean:
      if "또는" in i:
        mean.remove(i)
    # 문장
    txt = REMOVE(temp)
    sentence = Sentence(txt)


    choice = { name:value for name, value in zip(mean, example) }

    # json파일
    # 문제 2번은 WORD 굵은 글씨, (SENTENCE,MEAN) 문제, EXAMPLE 답 
    file_exam2 = OrderedDict()
    file_exam2["TYPE2"] = "위 지문의 '{}'은(는) 다의어이다. 각 문장에 사용된 '{}'의 의미로 알맞은 것을 고르시오.".format(word,word)
    file_exam2["WORD"] = word   #단어
    file_exam2["SENTENCE"] = sentence #단어가 있는 문장과 그 전후 문장
    #file_exam2["MEAN"] = mean   #뜻
    #file_exam2["EXAMPLE"] = example #용례
    file_exam2["CHOICE"] = choice

    #json파일
    EXAM2 = json.dumps(file_exam2, ensure_ascii=False, indent="\t")

    return EXAM2
