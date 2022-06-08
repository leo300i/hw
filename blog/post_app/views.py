from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from post_app.models import News, NewsComment
from post_app.forms import CreateNewsForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.


def test(request):
    return HttpResponse('<h1 style="color:red;">hello world!')


def test1(request):
    dict_ = {
        'title': 'Blog APPLICATION',
        'text': 'HELLO WORLD'
    }
    return render(request, 'hello.html', context=dict_)

@login_required(login_url='/login/')
def news_list_view(request):
    search_word = request.GET.get('search', '')
    news_list = News.objects.filter(title__icontains=search_word)
    context = {
        'news': news_list,
        'count': news_list.count()
    }
    return render(request, 'news.html', context=context)


def news_detail_view(request, id):
    try:
        news_detail = News.objects.get(id=id)
    except News.DoesNotExist:
        raise Http404('News not Found')
    comments = NewsComment.objects.filter(news_id=id)
    return render(request, 'news_detail.html', context={
        'detail': news_detail,
        'comments': comments
    })



@login_reqired(login_url='/login/')
def createNEWS_view(request):
    if request.method == 'GET':
        form = CreateNewsForm()
        return render(request, 'createNEWS.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = CreateNewsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news/')
        return render(request, 'createNEWS.html', context={
            'form': form
        })


def login_view(request):
    query = request.GET.get('next','/')
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(query)
    return render(request, 'login.html', context={
        'form': LoginForm(),
        'query': query
    })


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'register.html', context={
            'form': form
        })
    return render(request, 'register.html', context={
        'form': RegisterForm
    })
