from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html",{'name':'Aditya'})

def add(request):
    num1=request.POST["a"]
    num2=request.POST["b"]
    result=int(num1)+int(num2)
    return render(request,"result.html",{"result":result})