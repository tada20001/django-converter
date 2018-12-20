from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
]
