from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun3(request):
    return render(request,)
def fun4(request):
    return HttpResponse('<h1>This is the fun app 2 http Response content<h1>')