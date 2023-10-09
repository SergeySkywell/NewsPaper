from django.urls import path
from .views import NewsList, NewsDetail, Search, PostCreate, PostEdit, PostDelete, SignUp, subscriptions, IndexView

urlpatterns = [
   path('news/', NewsList.as_view(), name='news_list'),
   path('news/<int:pk>', NewsDetail.as_view()),
   path('news/search/', Search.as_view()),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('signup', SignUp.as_view(), name='signup'),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('', IndexView.as_view()),
]