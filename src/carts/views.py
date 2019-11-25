from django.shortcuts import render, redirect
from carts.models import Cart
from products.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import json
# Create your views here.

def add(id, user, count=1):
    pro = Product.objects.get(pk=id)
    cart = Cart.objects.filter(product=pro, user=user)
    if len(cart) == 0:
        instance = Cart.objects.create(user=user, cart_count=count)
        instance.product.add(pro)
        instance.save()
    else:
        cart= cart.first()
        print(cart.cart_count)
        cart.cart_count +=  count
        cart.save()


def AddToCart(request,id):
    add(id, request.user)
    return redirect('home')

@csrf_exempt
def AddCartMultiple(request):
    string = request.POST['items']
    items_hash = json.loads(string)
    for id in items_hash:
        add(id, request.user, int(items_hash[id]))
    cart_count = Cart.objects.filter(user=request.user).aggregate(Sum('cart_count'))
    return JsonResponse({'count': cart_count}, status=200)

@csrf_exempt
def cart_count(request):

    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).aggregate(Sum('cart_count'))
    else:
        cart_count=0
    return JsonResponse({"count": cart_count}, status=200)
