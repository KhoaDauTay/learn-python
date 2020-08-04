from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:photo_id>/', views.detail, name='detail'),
]
