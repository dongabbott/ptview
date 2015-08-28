#-*-coding:utf-8 -*-
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
import requests

# Create your views here.
def apilist(request):
    return render_to_response('api_list.html', {},   context_instance=RequestContext(request))

def apirun(request):
    if request.GET:
        url = request.GET['url']
        try:
            req = requests.get(url)
            body = req.text
        except Exception,e:
            body = e

    return render_to_response('api_list.html', {'body':body},   context_instance=RequestContext(request))