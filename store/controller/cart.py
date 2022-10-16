from django.contrib import messages
from django.shortcuts import render, redirect
from store.models import Servicemen, Cart
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required


def addtocart(request):
    # print("**************")
    if request.method =="POST":
        if request.user.is_authenticated:
            servicemen_id = int (request.POST.get('servicemen_id'))
            # print( servicemen_id , "********")
            servicemen_id_check = Servicemen.objects.get(id=servicemen_id)
            if (servicemen_id_check):
                # if(Cart.objects.filter(user=request.user.id, servicemen_id = servicemen_id)):
                #     return JsonResponse({'status':"You have added the person"})
                # else:
                Cart.objects.create(user = request.user,   servicemen_id= servicemen_id )
                return JsonResponse({'status':"Person added successfully"})

            else:
                return JsonResponse({'status':"No such serviceman found with that id "})
        else:
            return JsonResponse({'status':"login to continue"})
    return redirect("/")

@login_required(login_url='loginpage')
def viewcart(request):
    cart = Cart.objects.filter(user = request.user)
    context= {'cart': cart  }
    return render(request, "store/cart.html", context )