#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def home(request, template="home.html"):
    """
    Home page
    """
    return render_to_response(template, {}, RequestContext(request))  
    
    
    
