# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from simplemooc.courses.models import Course

#classe para representar as opções do curso
class CourseAdmin(admin.ModelAdmin):

#exibição por colunas das info do obj
    list_display = [
        'name',
        'slug',
        'start_date',
        'created_at'
    ]

    search_fields = [
        'name',
        'slug'
    ]
#autopreenchimento 
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Course, CourseAdmin)
