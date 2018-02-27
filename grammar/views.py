# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# 引入我们创建的表单类
from .forms import AddForm

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


def form_template(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'form_template.html', {'form': form})