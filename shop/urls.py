from .import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('allproducts/<str:n>/', views.details, name='details'),
    path('product/<str:p>/', views.product_details, name='product_details'),


]
