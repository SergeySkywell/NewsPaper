from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .filters import PostFilter
from .forms import PostForm, SignUpForm
from .models import Post, Subscriber, Category
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Exists, OuterRef
from django.core.cache import cache


class NewsList(ListView):
    model = Post
    queryset = Post.objects.filter(
        categoryType='NW'
    ).order_by('-dateCreation')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class Search(ListView):
    model = Post
    queryset = Post.objects.filter(
        categoryType='NW'
    ).order_by('-dateCreation')
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


class NewsDetail(DetailView):
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'product-{self.kwargs["pk"]}', None)

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'product-{self.kwargs["pk"]}', obj)
            return obj


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('accounts.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('accounts.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('accounts.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscriber.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )
