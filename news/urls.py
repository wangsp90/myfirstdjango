from django.urls import path
from . import views
app_name="news"

urlpatterns = [
    path('list/', views.news_list, name='newslist'),
    path('id/<newsid>/', views.news_id),
    path('search/', views.news_search)
]