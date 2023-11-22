from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun5(request):
    return render(request,'app3.html')

def fun6(request):
    return HttpResponse('<h2>This is app 3 http response view')
