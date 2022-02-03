import email
from http.client import HTTPResponse
from pickle import FALSE
from urllib import response
from django.shortcuts import render
from rest_framework import generics
import json
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['POST','GET'])
def SignUp(request) :
    file = {'result': 1}
    if request.method == 'POST':
        Post.objects.create(
            email = request.data['email'],
            name = request.data['name'],
            password = request.data['password'],
            affiliation= request.data['affiliation'],
            age= request.data['age']   
        )
        return JsonResponse(request.data, safe=False)
    return JsonResponse(file, safe=False)

@api_view(['POST','GET'])
def LogIn(request) :
    true = {'result': 1}
    false = {'result': 0}
    if request.method == 'POST':
        if Post.objects.filter(email = request.data['email']).exists():
            if Post.objects.filter(password = request.data['password']).exists():
                return JsonResponse(true, safe=False)
            else:
                return JsonResponse(false,safe=False)
        else:
            return JsonResponse(false, safe=False)
    return JsonResponse(false, safe=False)