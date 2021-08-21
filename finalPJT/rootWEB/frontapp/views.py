from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'front/index.html')

def scriptIndex(request):
    return render(request, 'front/script.html')

def idChkAjax(request) :
    print('frontApp idChkAjax~~~')
    id = request.POST['id']
    print('param ~ ' , id)
    list = [{'msg' : '확인'}]
    return JsonResponse(list , safe=False)

def staticFun(request):
    print('frontApp staticFun')
    return render(request,'front/static_page.html')

def navFun(request):
    print('frontApp navFun')
    return render(request,'front/navbar_page.html')

def bootFun(request):
    print('frontApp bootFun')
    return render(request,'front/boot_page.html')