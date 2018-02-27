# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse(u"django默认显示页面")


def intro(request):
    name = request.GET.get('name', 'python')
    day = request.GET.get('day', '10')
    return HttpResponse("学习" + name + "已经" + day + "天")


def simple(request):
    return render(request, 'simple.html')


def template_more1(request):
    string = "传递字符串参数到模板"
    return render(request, 'template_more1.html', {'string': string})


def template_more2(request):
    languages = ['php', 'java', 'python']
    return render(request, 'template_more2.html', {'languages': languages})


def template_more3(request):
    dict = {'category': '语言类', 'language': 'python'}
    return render(request, 'template_more3.html', {'dict': dict})


def template_more4(request):
    languages = ['php', 'java', 'python', 'django']
    return render(request, 'template_more4.html', {'languages': languages})


def template_more5(request):
    return render(request, 'template_more5.html')


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))