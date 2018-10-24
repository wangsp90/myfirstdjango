from django.urls import path
from . import views
app_name="news"

urlpatterns = [
    path('list/', views.news_list,name='newslist'),
    path('id/<newsid>/', views.news_id,name='newsid'),
    path('search/', views.news_search,name='search'),
    path('tpmif/', views.tpm_if),
    path('tpmfor/', views.tpm_for),
    path('', views.dtlurl)
]