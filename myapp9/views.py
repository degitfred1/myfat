from django.shortcuts import render

def gas(request):
    return render(request,'index.html1')

def who(request):
    return render(request,'index.html2')
