from . import views
from django.urls import include,path

urlpatterns = [
    path('', views.homepage, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('csrferror/', views.csrf_failure, name='csrferror')
]