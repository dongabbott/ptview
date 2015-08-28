#-*-coding:utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response('index.html', {},   context_instance=RequestContext(request))

def useradd(request):
    return render_to_response('login.html', {},   context_instance=RequestContext(request))