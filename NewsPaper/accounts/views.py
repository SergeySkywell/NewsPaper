from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .filters import PostFilter
from .forms import PostForm, SignUpForm
from .models import Post



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
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'


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
