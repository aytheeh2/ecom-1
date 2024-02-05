from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from .models import Category,Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    categories=Category.objects.all()
    return render(request,'category.html',{
        'categories':categories,
    })

def login_user(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            return HttpResponse('invalid user')
    return render(request,'login.html')

@login_required
def logout_user(request):
    logout(request)
    return home(request)


def details(request,n):
    # category = get_object_or_404(Category, name=n)
    category=Category.objects.get(name=n)
    product_details=Product.objects.filter(category=category)
    return render(request,'details.html',{
        'product_details':product_details,
        'category':category,
    })

def product_details(request,p):
    product=Product.objects.get(name=p)
    return render(request,'product_details.html',{
        'product':product,
    })