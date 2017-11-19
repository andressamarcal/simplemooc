# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Course

def index(request):
    courses = Courses.objects.all() #queryset
    template_name = 'courses/courses.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

def details(request, pk):
    pass
