from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from post_app.forms import CreateNewsForm, LoginForm
from post_app.models import News, NewsComment
from .models import Tag


def test(request):
    return HttpResponse('<h1 style="color:red;">Hello World!</h1>')


def test1(request):
    dict_ = {
        'title': 'Blog APPLICATION',
        'text': 'HELLO WORLD!',
        'date': ''
    }
    return render(request, 'hello.html', context=dict_)


PAGE_SIZE = 2


class NewsListView(ListView):
    queryset = News.objects.all()
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = PAGE_SIZE

    def get_queryset(self):
        qs = super(NewsListView, self).get_queryset()
        queryset = qs.filter(title__icontains=self.request.GET.get('search', ''))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsListView, self).get_context_data()
        context['word'] = self.request.GET.get('search', '')
        return context


@login_required(login_url='/login/')
def news_list_view(request):
    search_word = request.GET.get('search', '')
    page = int(request.GET.get('page', '1'))
    count_news = News.objects.filter(title__icontains=search_word).count()
    news_list = News.objects.filter(title__icontains=search_word)[PAGE_SIZE * (page - 1):PAGE_SIZE * page]
    if count_news % PAGE_SIZE != 0:
        page_count = count_news // PAGE_SIZE + 1
    else:
        page_count = count_news // PAGE_SIZE
    context = {
        'news': news_list,
        'count': news_list.count(),
        'word': search_word,
        'page_list': [page for page in range(1, page_count + 1)]
    }
    return render(request, 'news.html', context=context)


def news_detail_view(request, id):
    try:
        news_detail = News.objects.get(id=id)
    except News.DoesNotExist:
        raise Http404('News not FOUND!!!')
    comments = NewsComment.objects.filter(news_id=id)
    return render(request, 'news_detail.html', context={
        'detail': news_detail,
        'comments': comments
    })


@login_required(login_url='/login/')
def create_news_view(request):
    form = CreateNewsForm()
    if request.method == 'POST':
        form = CreateNewsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news/')
    return render(request, 'create_news.html', context={
        'form': form
    })


def login_view(request):
    print(request.GET)
    query = request.GET.get('next', '/')
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
        'form': RegisterForm()
    })


class TagListView(ListView):
    queryset = Tag.objects.all()
    template_name = 'tag_list.html'
    context_object_name = 'tags'