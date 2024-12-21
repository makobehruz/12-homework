from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def home(request):
    return render(request,'index.html')

def product_about(request):
    return render(request,'products/about.html')

def product_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request,'products/product-list.html', ctx)

def product_create(request):
    if request.method == 'POST':
        nomi = request.POST.get('nomi')
        tavsif = request.POST.get('tavsif')
        narxi = request.POST.get('narxi')
        image = request.FILES.get('image')
        kategoriya = request.POST.get('kategoriya')
        if nomi and tavsif and narxi and image and kategoriya:
            Product.objects.create(
                nomi=nomi,
                tavsif=tavsif,
                narxi=narxi,
                image=image,
                kategoriya=kategoriya,
            )
            return redirect('products:list')
    return render(request,'products/product-create.html')

def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    ctx = {'products': products}
    return render(request,'products/product-detail.html', ctx)

def product_category(request, category):
    products = Product.objects.filter(kategoriya=category)
    ctx = {
        'products': products,
        'category': category,
    }
    return render(request, 'products/product-list.html', ctx)
