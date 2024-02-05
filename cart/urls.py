from .import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('cartview',views.cartview,name='cartview'),
    path('addtocart/<str:p>',views.addToCart,name='addToCart'),
    path('subfromcart/<str:p>',views.subFromCart,name='subFromCart'),
    path('deletefromcart/<str:p>',views.deleteFromCart,name='deleteFromCart'),
    path('orderform/',views.orderform,name='orderform'),
    path('yourOrders/',views.yourOrders,name='yourOrders'),


]
