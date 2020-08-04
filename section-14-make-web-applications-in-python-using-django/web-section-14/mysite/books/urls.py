from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view( ), name='detail'),
    url(r"^books/add/$", views.BookCreateView.as_view(), name="book-add"),
    
]