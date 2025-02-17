from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name="home"),
    path('create', BlogCreate.as_view(), name="BlogCreate"),
    path('blog/<slug:slug>', BlogDetails, name="BlogDetails"),
    path('like/<slug:slug>', blogLike, name="blogLike"),
]
