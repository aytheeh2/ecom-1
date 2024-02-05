from django.shortcuts import redirect, render, HttpResponse

from shop.models import Product
from .models import Cart, Order, Account
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def cartview(request):
    u = request.user
    items = Cart.objects.filter(user=u)
    cart = Cart.objects.filter(user=u)
    cartTotal = 0
    for i in cart:
        cartTotal += i.quantity * i.product.price

    return render(request, 'cart.html', {
        'items': items,
        'cartTotal': cartTotal,
    })


@login_required
def addToCart(request, p):
    product = Product.objects.get(name=p)
    u = request.user

    try:
        cart = Cart.objects.get(user=u, product=product)
        if cart.quantity < cart.product.stock:
            cart.quantity += 1
            cart.save()
    except:
        if product.stock > 0:
            cart = Cart.objects.create(user=u, product=product, quantity=1)
            cart.save()
    return redirect('cart:cartview')


@login_required
def subFromCart(request, p):
    product = Product.objects.get(name=p)
    u = request.user

    try:
        cart = Cart.objects.get(user=u, product=product)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
    except:
        pass

    return redirect('cart:cartview')


@login_required
def deleteFromCart(request, p):
    product = Product.objects.get(name=p)
    u = request.user

    try:
        cart = Cart.objects.filter(user=u, product=product)
        cart.delete()
    except:
        pass

    return redirect('cart:cartview')


@login_required
def orderform(request):
    if request.method == "POST":
        user = request.user

        address = request.POST['address']
        phone = request.POST['phone']
        accNum = int(request.POST['accnum'])

        cart = Cart.objects.filter(user=user)
        total = 0
        for i in cart:
            total += i.quantity * i.product.price

        try:
            ACC = Account.objects.get(accnumber=accNum)
            if ACC.amount >= total:
                ACC.amount -= total
                ACC.save()
                for i in cart:
                    o = Order.objects.create(user=user, product=i.product, address=address,
                                             phone=phone, no_of_items=i.quantity, order_status='paid')
                    o.save()
                cart.delete()
                msg = 'Order Placed'
                return render(request, 'orderdetail.html', {
                    'msg': msg,
                })
            else:
                msg = 'Insufficient Balance'
                return render(request, 'orderdetail.html', {
                    'msg': msg,
                })

        except:
            pass
    return render(request, 'orderform.html')

@login_required
def yourOrders(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    return render(request,'yourOrders.html',{
        'orders':orders,
        'user':user,
    })