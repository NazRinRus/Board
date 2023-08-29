from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ads, Post, User
from .forms import AdsCreateForm, AdsUpdateForm, PostCreateForm, PostUpdateForm

# Create your views here.

menu = [{'title': ("О сайте"), 'url_name': 'about'},
        {'title': ("Обратная связь"), 'url_name': 'contact'},
        {'title': ("Войти / Зарегистрироваться"), 'url_name': '/accounts/login'}
]
class AdsList(ListView):
    model = Ads
    ordering = 'time_in'
    template_name = 'ads.html'
    context_object_name = 'ads'

    # получаю из адресной строки URL параметр position_ad - категория Ad для дальнейшей фильтрации
    def get_category(self, request):
        position_ad = request.GET.get("position_ad")
        return position_ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['menu'] = menu
        context['title'] = 'Все объявления'
        context['positions'] = Ads.POSITIONS # список всех категорий для меню
        context['position_ad'] = self.get_category(self.request) # выбранная категория
        return context

class AdDetail(DetailView):
    model = Ads
    template_name = 'ad.html'
    context_object_name = 'ad'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем объект Ads для текущего представления
        ads_object = self.object
        # Отфильтровываем записи Post связанные с текущим объектом Ads
        context['posts'] = Post.objects.filter(post_at_ad=ads_object)
        context['menu'] = menu
        context['title'] = 'Объявление'
        context['positions'] = Ads.POSITIONS
        return context

class AdCreate(CreateView):
    form_class = AdsCreateForm
    model = Ads
    template_name = 'ad_edit.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = ('Создание объявления')
        context['positions'] = Ads.POSITIONS
        return context

class PostCreate(CreateView):
    form_class = PostCreateForm
    model = Post
    template_name = 'post_edit.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = ('Создание объявления')
        context['positions'] = Ads.POSITIONS
        context['user'] = self.request.user.username
        context['post_id'] = int(self.request.path.split('/')[1])
        return context
    def form_valid(self, form):
        post = form.save(commit=False)
        ad_id = int(self.request.path.split('/')[1])
        ad = Ads.objects.filter(pk=ad_id)
        post.post_at_ad = ad[0]
        username = self.request.user.username
        print(username)
        user1 = User.objects.filter(username=username)
        post.author_post = user1[0]
        post.save()
        return super().form_valid(form)



def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О сайте'})