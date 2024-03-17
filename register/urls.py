from django.urls import path
from . import views

urlpatterns = [
    path('logout-page/', views.logout_view, name='logout-page'),
    path('login-view', views.login_view, name='login-page'),

]