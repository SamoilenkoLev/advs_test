# coding: utf-8
from .models import *
from django.views.generic import DetailView, ListView


class List(ListView):
    model = Advs


class Detail(DetailView):
    model = Advs
