from django.contrib import messages
from django.shortcuts import render, redirect
from store.models import Cart ,Order, OrderItem, Product 
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import random
from store.models import Cart

@login_required(login_url='loginpage')
def index(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0 
    for item in cartitems:
        total_price = total_price + item.servicemen.price
    context = {'cartitems' : cartitems , 'total_price': total_price}
    return render(request, "store/checkout.html",context)


@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':
        # get users details from users table for autofill table
        # currentuser = User.objects.filter(id=request.user.id).first()
        
        # if not currentuser.first_name: 
        #     currentuser.first_name = request.POST.get('fname')
        #     currentuser.last_name = request.POST.get('lname')
        #     currentuser.save() 

        # if not Profile.objects.filter(user=request.user):
        #     userprofile = Profile()
        #     userprofile.user = request.user
        #     userprofile.phone = request.POST.get('phone')
        #     userprofile.address = request.POST.get('address')
        #     userprofile.city = request.POST.get('city')
        #     userprofile.state = request.POST.get('state')
        #     userprofile.country = request.POST.get('country')
        #     userprofile.pincode = request.POST.get('pincode')
        #     userprofile.save()
             

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        
        neworder.country = request.POST.get('country')
        

        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.servicemen.price

        neworder.total_price = cart_total_price
        trackno = 'db'+str(random.randint(1111111,9999999))
        # ensure tracking number always remain unique 
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'db'+str(random.randint(1111111,9999999))

        neworder.tracking_no = trackno 
        neworder.save() 

        neworderitems = Cart.objects.filter(user = request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                user = request.user, 
                outlet=item.outlet,
                servicemen = item.servicemen,
                menuitem = item.menuitem

            )   

            # To decreatse the product quantity  from available stock 
            # orderproduct = Product.objects.filter(id=item.product_id).first()
            # orderproduct.quantity = orderproduct.quantity - item.product_qty
            # orderproduct.save()

        # to clear user's cart 
        Cart.objects.filter(user = request.user).delete()


        # payMode = request.POST.get('payment_mode')

        # if payMode == "Paid by Razorpay" or "Paid by Paypal":
        #     return JsonResponse({'status':"Your order has been placed successfully"})
        # else:
        messages.success(request, "Your order has been placed successfully")

    return redirect('/home')