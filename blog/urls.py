
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show,name='show'),
    path('<int:blog_id>/',views.detail,name='detail'),


]
