from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('login/dashboard/<int:id>', views.dashboard, name="dashboard"),
    path('result/', views.result, name="result"),
    path('activity/', views.activity, name="activity"),
    path('assignments/', views.assignment, name="assignments"),
    path('profile/', views.profile, name="personalinfo"),
    path('logout/', views.logout_view, name="logout"),
    # path('login/form/', views.studnt, name="studentform"),
]