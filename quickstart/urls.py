from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('home2/', views.httpresponse),
    path('json/', views.jsonresponse),
    path('file/', views.fileresponse),
    path('template/', views.httptemplate),
    path('message/', views.messages),
    path('hello/', views.hello)
]