from django.shortcuts import render,redirect
from . models import *
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request , 'store/index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category }
    return render(request , "store/collections.html", context)


def collectionsview(request , slug):
    if(Category.objects.filter(slug=slug , status =0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug = slug).first()
        context= {'products': products , 'category': category }
        return render(request, "store/products/index.html" , context )
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')



def productview(request , cate_slug , prod_slug):
    # check if category slug exist or not  
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0)
            context = {'products': products}
        else: 
            messages.error(request, "No such category found ")
            return redirect('collections')
    else: 
        messages.error(request, "No such category found ")
        return redirect('collections')
    return render(request , "store/products/view.html", context )
    
def cluster (request, location):
    # outlets = Outlets.objects.all()
    outlets = Outlets.objects.filter(location__name = location)
    servicemen = Servicemen.objects.filter(location__name = location)
    menuitem = Menuitem.objects.filter(location__name = location)
    context = {'outlets': outlets, 'servicemen': servicemen , 'menuitem': menuitem , 'location':location }
    return render(request , "store/tripleitems/cluster.html", context)


def locationListAjax(request  ) :
    location = Location.objects.all().values_list('name', flat=True)
    locationList = list (location )
    return JsonResponse (locationList  ,safe = False)


def searchLoc(request):
    if request.method =="POST":
        searchedLocation = request.POST.get('locationSearch')
        # if searchedLocation is none then redirect back  
        if searchedLocation == "":
            return  redirect(request.META.get('HTTP_REFERER'))
        else: 
            return redirect('cluster/'+searchedLocation)

    # get the previous page address 
    return redirect (request.META.get('HTTP_REFERER'))


def outletDetail(request, id):
    outlets = Outlets.objects.filter(id = id ).first()

    # get the name of  location of the outlet 
    locationName = outlets.location
    # get the id of  location name
    locationId = Location.objects.filter(name=locationName)[0].id
    # get menuitem(s) found in that outlet  
    menuitemInthisOutlet = Menuitem.objects.filter(outlet_id = locationId)

    servicemen = Servicemen.objects.filter(outlet__id = id) 
    context = {'outlets': outlets , 'servicemen': servicemen , 'menuitemInthisOutlet': menuitemInthisOutlet }
    return render(request , "store/tripleitems/outlets/outletsDetail.html", context)


