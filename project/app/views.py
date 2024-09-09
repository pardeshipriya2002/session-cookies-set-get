from django.shortcuts import render

# Create your views here.
from datetime import *

def set(request):
    data =render(request,'set.html')
    data.set_cookie('name','priya', max_age=2*24*60*60, httponly=True,secure=True)
    data.set_cookie('age','20',max_age=4*24*60*60, httponly=True,secure=True)
    data.set_cookie('city','Bhopal',max_age=3*24*60*60, httponly=True,secure=True)

    return data

def get(request):
    print(request.COOKIES)
    nm = request.COOKIES['name']
    ag = request.COOKIES['age']
    ct = request.COOKIES['city']

    data ={

        'name': nm,
        'age': ag,
        'city': ct,

    }

    return render(request,'get.html',data)
 