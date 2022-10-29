from django.urls import path
from . import views
# the url by default is /products because we are in the products application
urlpatterns = [
    path('', views.index),
    path('new/', views.new),

]