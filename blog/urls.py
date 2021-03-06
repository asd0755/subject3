from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.read, name='read'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
]