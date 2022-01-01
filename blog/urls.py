from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('post/create/', views.post_create, name='post_create'),
]