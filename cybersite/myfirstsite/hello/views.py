from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from hello.forms import *

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404
from hello.models import *
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from django.forms import model_to_dict


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data)

    
class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#class PostAPIView(APIView):
#    def get(self, request):
#        lst = Post.objects.all().values()
#        return Response({'posts': PostSerializer(lst, many=True).data})
#    
#    def post(self, request):
#        serializer = PostSerializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#
#        return Response({'post': model_to_dict(serializer.data)})
    

menu = [{'title': 'Мы', 'url_name': 'about'},
        {'title': 'Добавить', 'url_name': 'addpage'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


class PostHome(ListView):
    model = Post
    template_name = 'hello/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context


#class PostAPIView(generics.ListAPIView):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer
    

class CategoryHome(ListView):
    model = Post
    template_name = 'hello/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat_id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'hello/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_lsit=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context
    

class ShowPage(DetailView):
    model = Post
    template_name = 'hello/mini_index.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_lsit=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'hello/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_lsit=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Киберспорт КФУ',
        'cat_selected': 0
    }
    return render(request, 'hello/index.html', context=context)

def about(request):
    return render(request, 'hello/about.html', {'menu': menu, 'title': 'О нас'})

def login(request):
    return HttpResponse("Авторизация")

def register(request):
    return HttpResponse("Регистрация")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'hello/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    context = {
        'post': post,
        'menu': menu,
        'title': 'Отображение поста'
    }
    return render(request, 'hello/mini_index.html', context=context)


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'hello/index.html', context=context)


def addpage(request):
    if request.method == 'POST':    
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'hello/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
