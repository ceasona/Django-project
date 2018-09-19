
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home ,name='home'),
    path('market', views.home, name='market'),
    path('cart', views.home, name='cart'),
    path('mine', views.home, name='mine'),
]