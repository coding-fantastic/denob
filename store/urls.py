from django.urls import path 
from . import views
from store.controller import authview ,cart ,checkout , order

urlpatterns = [
    path('home' ,views.home, name='home'),
    path('', authview.loginpage , name='loginpage'),
    path('collections' ,views.collections, name='collections'),
    path('collections/<str:slug>' ,views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>' ,views.productview, name='productview'),

    path('location-list', views.locationListAjax),
    path( 'searchLoc' , views.searchLoc, name="searchLoc" ), 

    # authentication 
    path('register', authview.register , name='register'),
    path('login', authview.loginpage , name='loginpage'),
    path('logout', authview.logoutpage , name='logout'),

    path('cluster/<str:location>' ,views.cluster, name='cluster'),
    path('outletDetail/<str:id>', views.outletDetail, name='outletDetail'),

    path('add-to-cart', cart.addtocart, name ='addtocart'),
    path('cart', cart.viewcart, name ='cart'),

    path('checkout', checkout.index, name ='checkout'),
    path('place-order', checkout.placeorder, name ='placeorder'),

    path('my-orders', order.index, name ='myorders'),
    path('view-order/<str:t_no>', order.vieworder , name="orderview"),


    
]
