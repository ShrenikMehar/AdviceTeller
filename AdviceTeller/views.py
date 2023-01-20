from django.http import HttpResponse
from django.shortcuts import render
from AdviceTeller import generate

def index(request):
    if request.method == 'GET':
        advice = generate.randomadvice(0)
        data={
            'title':'Advice Teller by Shrenik',
            'advice':advice
        }
        return render(request,"index.html",data)
    else:
        return render(request,"index.html",data)
