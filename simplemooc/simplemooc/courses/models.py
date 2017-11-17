# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.CharField('Atalho', max_length=20)
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Ínicio', null=True, blank=True
    )
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )
