from .models import Backlink_cart

def cart_count(request):
    if request.user.is_authenticated:
        count = Backlink_cart.objects.filter(user=request.user,is_paid=False).count()
    else:
        count = 0
    return {'cart_count': count}
