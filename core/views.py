from django.shortcuts import render, redirect
from core.models import Product
from core.forms import UserRegisterForm
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    context = {
        "products":products
    }
    return render(request, 'core/index.html', context)

def register_view(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
        
    else:
        form = UserRegisterForm()

    
    context = {
        'form': form,
    }
    return render(request, "core/sign-up.html", context)