from .models import Cart
def itemsInCart(request):
    cartItems=0
    u=request.user
    try:
        cart=Cart.objects.filter(user=u)
        for i in cart:
            cartItems+=i.quantity
    except:
        cartItems=0
    return {'cartItems':cartItems,}



# def total(request):
#     item_count=0
#     if request.user:
#         u=request.user
#     try:
#         cart=Cart.objects.filter(user=u)
#         for i in cart:
#             item_count+=i.quantity
#     except:
#         item_count=0

#     return {'count':item_count}