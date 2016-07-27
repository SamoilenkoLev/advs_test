# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Advs(models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return reverse('advs-detail', kwargs={'pk': self.pk})
