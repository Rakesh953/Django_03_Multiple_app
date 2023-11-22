from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return render(request,'app1.html')

def fun2(request):
    return HttpResponse('<h1>This is the fun app 1 http Response content<h1>')