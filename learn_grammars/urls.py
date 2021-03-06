"""learn_grammars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from grammar import views as grammar_views

urlpatterns = [
    url(r'^intro/$', grammar_views.intro, name='intro'),
    url(r'^simple/$', grammar_views.simple, name='simple'),
    url(r'^template_more1/$', grammar_views.template_more1, name='template_more1'),
    url(r'^template_more2/$', grammar_views.template_more2, name='template_more2'),
    url(r'^template_more3/$', grammar_views.template_more3, name='template_more3'),
    url(r'^template_more4/$', grammar_views.template_more4, name='template_more4'),
    url(r'^template_more5/$', grammar_views.template_more5, name='template_more5'),
    url(r'^add/(\d+)/(\d+)/$', grammar_views.add, name='add'),
    url(r'^forms/$', grammar_views.form_template, name='form'),
    url(r'^$', grammar_views.index),
    url(r'^admin/', admin.site.urls),
]
