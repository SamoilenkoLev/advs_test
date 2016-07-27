# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.core.cache import cache


SESSION_CACHE_KEY = 'ads_{}_sessions'
VIEW_CACHE_KEY = 'ads_{}'


class Advs(models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    name = models.CharField('Название', max_length=200)
    text = models.TextField('Текст')
    view = models.IntegerField('Количество просмотров', default=0)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return reverse('advs-detail', kwargs={'pk': self.pk})

    def get_view(self):
        view_key = VIEW_CACHE_KEY.format(self.pk)
        view = cache.get(view_key)
        if not view:
            view = self.view
            cache.set(view_key, view)
        return view

    def incr_view(self, session):
        sessions_key = SESSION_CACHE_KEY.format(self.pk)
        view_key = VIEW_CACHE_KEY.format(self.pk)

        ads_sessions = cache.get(sessions_key, [])
        if session not in ads_sessions:
            cache.set(view_key, self.get_view()+1)
            ads_sessions.append(session)
            cache.set(sessions_key, ads_sessions)
