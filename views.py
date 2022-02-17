from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import torch
from transformers.models.bart import BartForConditionalGeneration
from transformers import PreTrainedTokenizerFast
import json
from collections import OrderedDict
import random 
from rest_framework.decorators import api_view

# Create your views here.
model = BartForConditionalGeneration.from_pretrained('./kobart_summary')
tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v1')
    
@api_view(['POST','GET'])
def models(request) :
    
    #지문(text)을 임시적으로 로컬에 있는 파일로 불러왔습니다!
    text = ""
    f = open("./text.txt", "r", encoding = "utf-8")
    while True:
        line = f.readline()
        if not line: break
        text += line
    f.close()

    #지문(text)를 요약하는 과정(요약결과:output)
    text = text.replace('\n', '')
    input_ids = tokenizer.encode(text)
    input_ids = torch.tensor(input_ids)
    input_ids = input_ids.unsqueeze(0)
    output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
    output = tokenizer.decode(output[0], skip_special_tokens=True)

    #요약결과(output)를 토대로 문제 생성    
    content = output.split(' ')
    answerlist = []
    for i in range(len(content) - 1):
        if i % 2 == 0:
            answerlist.append(content[i]+" "+content[i+1])
    if len(content) % 2 != 0:
        answerlist.append(content[len(content)-1])
    text= text.replace('.', ' ')
    randoms = text.split(' ')
    randomlist = []
    for i in range(len(randoms) - 1):
        if i % 2 == 0:
            randomlist.append(randoms[i]+" "+randoms[i+1])
    randomlist = random.sample(randomlist,len(answerlist))
    answerlist += randomlist
    random.shuffle(answerlist)

    file_data = OrderedDict()
    #content: 블록배열을 위한 단어배열(본문 속 무작위 단어 + 요약문 단어)
    file_data["content"] = answerlist
    #answer: 요약문 정답
    file_data["answer"] = output
    #json파일(DB에 저장할 json파일 생성)
    jsonfile = json.dumps(file_data, ensure_ascii=False)
    
    #DB에 저장하는 과정 필요
    
    return HttpResponse(jsonfile)