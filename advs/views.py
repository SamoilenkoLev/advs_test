# coding: utf-8
from .models import *
from django.views.generic import DetailView, ListView


class List(ListView):
    model = Advs


class Detail(DetailView):
    model = Advs

    def get_object(self):
        obj = super(Detail, self).get_object()
        obj.incr_view(self.request.session.session_key)
        return obj
