from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('login/', views.Login, name="login"),
    path('register/', views.signup, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('login/activities/', views.activity, name="activities"),
    path('login/result/', views.result, name="result"),
]
