from django.urls import path
from . import views
from django.conf import settings
from django.templatetags.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.signup, name="register"),
]
