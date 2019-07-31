from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createp, name='createp'),
    path('', views.read, name='readp'),
    path('update/<int:pk>', views.update, name='updatep'),
    path('delete/<int:pk>', views.delete, name='deletep'),
    path('detail/<int:pk>', views.detail, name='detailp'),
]