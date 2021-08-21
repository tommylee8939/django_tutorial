from django.shortcuts import render, redirect

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    if request.session.get('user_name'):
        context = {
            'session_user_name': request.session['user_name'],
            'session_user_id': request.session['user_id']
        }
        return render(request,'bbs/home.html',context)
    return render(request, 'bbs/login.html')



# select * from bbsuser where user_id = ...
# orm : modelName.objects.get()
# orm : modelName.objects.all()
def login(request):
    if request.method =='POST':
        id = request.POST['id']
        pwd = request.POST['pwd']
        user = BbsUser.objects.get(user_id = id,user_pwd = pwd)
        print('user result :',user)
        context={}
        if user is not None :
            # 세션을 만드는 과정
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_name
            # 세션을 심는 과정
            context['session_user_name'] = request.session['user_name']
            context['session_user_id'] = request.session['user_id']
            return render(request,'bbs/home.html',context)

def logout(request):
    request.session['user_name'] = {}
    request.session['user_id'] = {}
    request.session.modified = True
    return redirect('main')

def registerForm(request):
    return render(request,'bbs/join.html')

def register(request):
    if request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['pwd']
        name = request.POST['name']
        print('user result :', id,pwd,name)
        BbsUser(user_id = id,user_pwd =pwd,user_name = name).save()
    return redirect('main')




# post
# ORM : modelName.objects.all()로 전체를 다 가져올 수 있다
# 가져온 테이블을 세션에 심을 필요는 없고 뿌려주면 된다
# 테이블이 많으면 루프를 돌리자
#
def list(request):

    # if request.method == 'POST':
    #     title = request.POST['title']
    #     content = request.POST['content']
    #     writer = request.POST['writer']
    #     Bbs(title=title,content = content,writer=writer).save()

    posts = Bbs.objects.all()
    context = {
        'posts': posts,
        'session_user_name': request.session['user_name'],
        'session_user_id': request.session['user_id']
    }
    return render(request,'bbs/list.html',context)


def bbsForm(request):
    print('bbsForm')
    context = {
        'session_user_name': request.session['user_name'],
        'session_user_id': request.session['user_id']
    }
    return render(request,'bbs/bbsRegisterForm.html',context)


def bbsRegister(request):

    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    Bbs(title=title, content=content, writer=writer).save()

    return redirect('list')

def bbsRead(request,id): # 장고만의 방식이 있다는것을 알아두자
    # id = request.GET['id']
    bbs = Bbs.objects.get(id=id)
    bbs.viewcnt+=1
    bbs.save()
    context = {
        'post':bbs ,
        'session_user_name': request.session['user_name'],
        'session_user_id': request.session['user_id']
    }
    return render(request,'bbs/read.html',context)

def bbsDelete(request):
    id = request.GET['id']
    bbs = Bbs.objects.get(id=id)
    bbs.delete()
    return redirect('list')

def bbsAdjust(request):
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    print(content)

    bbs = Bbs.objects.get(id=id)
    bbs.title = title
    bbs.content = content
    bbs.save()
    print('왜 print가안되지')
    return redirect('list')

# select *from table where title like '%공지%'
# select *from table where title like '공지%'
# select *from table where title like '공지%'

# model.objects.filter(title_icontains='공지')
# model.objects.filter(title_startswith='공지')
# model.objects.filter(title_endtswith='공지')

def bbsSearch(request):
    print('bbsSearch 진입')
    type = request.POST['type']
    keyword = request.POST['keyword']
    print(type,keyword)

    if type=='title':
        posts = Bbs.objects.filter(title__icontains = keyword)
    else:
        posts = Bbs.objects.filter(writer__startswith = keyword)
    print(posts)
    postLists = []
    for post in posts:
        postLists.append({
            'id' : post.id,
            'title' : post.title,
            'writer' : post.writer,
            'regdate' : post.regdate,
            'viewcnt' : post.viewcnt
        })
    print(postLists)
    return JsonResponse(postLists,safe=False)