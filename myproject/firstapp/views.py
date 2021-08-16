from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'name' : 'Kanghee Lee',
        'age': 23,
        'nationality' : 'Korean'
    }
    return render(request,'index.html',context)

