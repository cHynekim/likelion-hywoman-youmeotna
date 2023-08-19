from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Shipping

# Create your views here.

@login_required
def shipping(request):
    user = request.user
    my_shippings = Shipping.objects.filter(user=user)

    transit_shippings = Shipping.objects.filter(user=user, status='in_transit').select_related('bundle')
    delivered_shippings = Shipping.objects.filter(user=user, status='delivered').select_related('bundle')
    context = {
        'transit_shippings': transit_shippings,
        'delivered_shippings': delivered_shippings,
        'my_shippings': my_shippings,
    }

    return render(request, 'shipping/tracking.html', context)
