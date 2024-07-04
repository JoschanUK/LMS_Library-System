from . import views
from django.urls import path

urlpatterns = [
    #path('', views.PostList.as_view(template_name="main/booklist.html"), name='main'),
    path('', views.PostList.as_view(), name='main'),
]