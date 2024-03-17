from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home-char'),
    path('create/',views.create, name='create-char'),
    path('my_characters/',views.characters, name='characters-char'),
    path('home/',views.home, name='home-char'),
    path('<int:id>', views.index, name='index'),
    path('characters/', views.allchar, name='allchar-char'),
    path('contrib/',views.contrib, name='contrib'),
]