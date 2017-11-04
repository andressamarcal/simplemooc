# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, 'template/home.html')

def contact(request):
    return render(request, 'template/contact.html')
