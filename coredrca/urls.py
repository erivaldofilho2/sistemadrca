from django.conf.urls import url
from coredrca import views

urlpatterns = [
    url(r'^$', views.home),  
    url(r'^alunos$', views.alunos),         
]