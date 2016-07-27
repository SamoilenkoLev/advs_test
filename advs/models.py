# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Advs(models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
