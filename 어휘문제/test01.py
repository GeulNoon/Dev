from exam_word import word_01
from exam_func import TEST, MEAN,EXAMPLE, EXAMPLE_test
import json
from collections import OrderedDict

#exam_word에서 뽑아온 1번문제 어휘
word = word_01

#parsing에서 코드 추출
t = TEST(word)
result_parse = t[0]
result_example = t[1]

# 뜻 추출
ex_mean = MEAN(result_parse)
# 용례 추출
ex_example = EXAMPLE(result_example)
# 빈칸 문제 생성
ex_test = EXAMPLE_test(ex_example)

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
test = REMOVE(ex_test)


#json파일
#문제 1번은 TEST1이 문제, 정답은 WORD, 해설은 MEAN
file_exam1 = OrderedDict()
file_exam1["TYPE1"] = "다음 단어 중 빈칸에 들어갈 수 있는 단어를 고르시오."
file_exam1["WORD"] = word    #단어
file_exam1["TEST1"] = test   #문제
file_exam1["MEAN"] = mean    #뜻

#json파일
EXAM1 = json.dumps(file_exam1, ensure_ascii=False, indent="\t")
