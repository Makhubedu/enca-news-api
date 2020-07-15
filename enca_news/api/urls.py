from django.urls import path
from . import views

urlpatterns = [
    path('', views.api, name='api'),
    path('header/category/<str:category>', views.main_news, name="main_news"),
    path('body/category/<str:category>',views.body_news,name="body-news"),
    path('read', views.read_news,name="read")
]
