from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listings
from realtors.models import Realtor
from listings.choices import state_choices,price_choices,bedroom_choices


def index(request):

    listings=Listings.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
    'listings':listings,
    'bedroom_choices':bedroom_choices,
    'state_choices':state_choices,
    'price_choices':price_choices,
    }

    return render(request,'pages/index.html',context)

def about(request):
    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    #get mvp realtors
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context={
    'realtors':realtors,
    'mvp_realtors':mvp_realtors,
    }
    return render(request,'pages/about.html',context)
