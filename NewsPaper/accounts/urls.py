from django.urls import path
from .views import NewsList, NewsDetail, Search, PostCreate, PostEdit, PostDelete

urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', NewsDetail.as_view()),
   path('search/', Search.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]