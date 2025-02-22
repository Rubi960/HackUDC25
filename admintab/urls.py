from . import views
from django.urls import include,path

urlpatterns = [
    path('', views.admin_view, name='admin'),
]
