from django.shortcuts import render
from core.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    context = {
        "products":products
    }
    return render(request, 'core/index.html', context)
