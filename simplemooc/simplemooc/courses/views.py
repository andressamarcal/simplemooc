# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse

def index(request):
    courses = Courses.objects.all() #queryset
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

'''def details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    template_name = 'courses/details.html'
    context = {
        'course': course
    }
    return render(request, template_name, context)'''

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    template_name = 'courses/details.html'
    context = {
        'course': course,
        'form': ContactCourse()
    }
    return render(request, template_name, context)
