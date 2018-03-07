from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,render,get_object_or_404
from .loginform import LoginForm
# Create your views here.

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html')
    else:
        return HttpResponse("hello world")
