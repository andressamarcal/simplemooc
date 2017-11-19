# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


#model para poder manusear as querysets
#o metodo searh fara uma busca no nome e na descrição
class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.CharField('Atalho', max_length=20)
    description = models.TextField('Descrição Simples', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField(
        'Data de Ínicio',
        null=True,
        blank=True
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
    #essa classe terá agora o manager customizado e implementado acima, como seu gerenciador
    objects = CourseManager()

    #exibindo para o usuario o nome dos cursos na listagem do admin
    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'curso'
        verbose_name_plural= 'cursos'
        ordering = ['name']
