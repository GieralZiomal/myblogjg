from django.urls import path

from . import views

urlpatterns = [

    path('', views.mainpage, name="home"),
    path('blog/', views.blog, name="blog"),
    path('article/<int:id>', views.dynamic_lookup_view, name="article")

]