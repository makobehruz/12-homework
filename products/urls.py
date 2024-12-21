from django.urls import path
from . import views


app_name = 'products'


urlpatterns = [
    path('about/', views.product_about, name='about'),
    path('list/', views.product_list, name='list'),
    path('create/', views.product_create, name='create'),
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('category/<str:category>/', views.product_category, name='category'),
]