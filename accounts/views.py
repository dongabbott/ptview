#-*-coding:utf-8 -*-
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse

def login(request):
    err = ""
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                err = u"您的帐号已经被禁用，请联系管理员！"
        else:
            err = u"用户名或密码错误，请重新登录！"
    return render_to_response('login.html', {'username':username, 'err':err},   context_instance=RequestContext(request))

def userlist(request):
    user_list = User.objects.all()
    return render_to_response('user_list.html', {'user_list':user_list},   context_instance=RequestContext(request))