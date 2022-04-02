import requests
from bs4 import BeautifulSoup

word = ""
urls = "https://krdict.korean.go.kr/api/search?"
urlv = "https://krdict.korean.go.kr/api/view?"
serviceKey = "certkey_no=3349&key=EAE8B2C9214D808997D177C50333BBFA"
typeOfSearch_s="&type_search=search"
typeOfSearch_v = "&type_search=view"
part = "&part=word"
sort = "&sort=popular"
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
method = "&method=TARGET_CODE"

def TEST(word):
    def parse():
        try:
            TGT = item.find("target_code").get_text()
            WORD = item.find("word").get_text()
            DEF = item.find("definition").get_text()
            return {
                    "코드":TGT,
                    "단어":WORD,
                    "뜻":DEF,
                    }

        except AttributeError as e:
            return {
                "코드":None,
                "단어":None,
                "뜻":None,
            }
    def target_parse():
        try:
            TGT = item.find("target_code").get_text()
            return {
                TGT,
            }

        except AttributeError as e:
            return {
                None,
            }
    #parsing 하기
    result = requests.get(urls+serviceKey+typeOfSearch_s+part+"&q="+word+sort, verify=False)
    soup = BeautifulSoup(result.text,'lxml-xml')
    items = soup.find_all("item")

    parsing_result = []
    for item in items:
        WORD = item.find("word").get_text()
        if WORD == word:
            parsing_result.append(parse())

    target_row = []
    for item in items:
        WORD = item.find("word").get_text()
        if WORD == word:
            target_row.append(str(target_parse())[2:7])

    #용례 가져오기
    def parse2():
        try:
            CODE = item.find("target_code").get_text()
            EX = item.find("example").get_text()
            return {
                    "코드":CODE,
                      "용례":EX,
                    }

        except AttributeError as e:
            return {
                "코드":None,
                "용례":None,
            }
    example_result = []
    for code in target_row:
        word2 = code
        result2 = requests.get(urlv+serviceKey+typeOfSearch_v+method+part+"&q="+word2+sort, verify=False)
        soup = BeautifulSoup(result2.text,'lxml-xml')
        items2 = soup.find_all("item")

        for item in items2:
            example_result.append(parse2())
            
    return parsing_result, example_result
            
# st = parsing_result
# 뜻
def MEAN(st):
    mean = []
    for item in st:
        mean.append(str(item)[34:])
    return mean

# st = example_result
# 예문
def EXAMPLE(st):
    example = []
    for item in st:
        example.append(str(item)[22:])
    return example

# st = EXAMPLE의 결과
# 예문빈칸
def EXAMPLE_test(st):
    example = []
    for item in st:
        val = item.find(word)
        string = item[:val] + "____" + item[val+len(word):]
        example.append(string)
    return example