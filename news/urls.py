from django.urls import path
from . import views
app_name="news"

urlpatterns = [
    path('list/', views.news_list,name='newslist'),
    path('id/<newsid>/', views.news_id,name='newsid'),
    path('search/', views.news_search,name='search'),
    path('tpmif/', views.tpm_if,name='tpmif'),
    path('tpmfor/', views.tpm_for,name='tpmfor'),
    path('addview/', views.add_view,name='addview'),
    path('cut/', views.cut_view,name='cut'),
    path('date/', views.date_view,name='date'),
    path('', views.dtlurl)
]