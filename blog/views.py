from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("안녕하세요")
