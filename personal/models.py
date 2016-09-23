# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from firebase import firebase

# Create your models here.

firebase = firebase.FirebaseApplication('https://speechtolatex.firebaseio.com/', None)
users_dir = '/users'

def get_unique_code(timestamp):
    """ given a timestamp,
    get the unique code for
    that timestamp
    """
    return timestamp[-4:] + str(abs(hash(timestamp)) / 10000000000000000)

def delete_timestamp(timestamp):
    firebase.delete(users_dir, timestamp)

def create_new_user():
    new_user = {'speech':'', 'latex':'', 'url':''}
    result = firebase.post(users_dir, new_user)
    timestamp = result['name']
    uc = get_unique_code(timestamp)
    delete_timestamp(timestamp)
    result = firebase.put(users_dir, uc, new_user)
    return uc



