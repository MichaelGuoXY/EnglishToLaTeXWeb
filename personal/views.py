# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    result = models.create_new_user()
    return render(request, 'personal/home.html', {'content':[result]})

