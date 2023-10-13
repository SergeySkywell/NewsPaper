from django.urls import path
from .views import NewsList, NewsDetail, Search, PostCreate, PostEdit, PostDelete, SignUp, subscriptions
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('news/', cache_page(60)(NewsList.as_view()), name='news_list'),
   path('news/<int:pk>', cache_page(60*5)(NewsDetail.as_view())),
   path('news/search/', Search.as_view()),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('signup', SignUp.as_view(), name='signup'),
   path('subscriptions/', subscriptions, name='subscriptions'),
]