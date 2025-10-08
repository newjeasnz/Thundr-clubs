from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)
        
    form = ProductForm()

    context = {
        'app_name': 'THUNDR clubs',
        'name': request.user.username,
        'npm': '2406355445',
        'class': 'PBP B',
        'product_list': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'form': form,
    }

    return render(request, "main.html", context)

# TODO: ubah ke ajax
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')
    
    context = {
        'form': form
        }
    return render(request, "create_product.html", context)

# TODO: ubah ke ajax
@login_required(login_url='/login')
def show_detail_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "detail_product.html", context)
    

def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products = Product.objects.all()
    data = [
        {'id': str(product.id), 
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            }
        for product in products
    ]
    return JsonResponse(data, safe=False)

def show_xml_id(request, id):
    data = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_id(request, id):
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

# TODO: ubah ke ajax
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# TODO: ubah ke ajax
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# TODO: ubah ke ajax
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form' : form
    }

    return render(request, "edit_product.html", context)

# TODO: ubah ke ajax
def delete_product(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)

        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'You are not authorized to delete this product.'}, status=403)

        product.delete()

        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405) # 405 = Method Not Allowed

@csrf_exempt
@require_POST
def add_product_ajax(request):
    if request.method == 'POST':
        # Mengambil setiap data secara manual dari request.POST
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        
        # Penanganan untuk checkbox 'is_featured'
        is_featured = request.POST.get("is_featured") == 'on'
        
        user = request.user

        # Membuat objek Product baru secara manual
        new_product = Product(
            name=name, 
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            user=user
        )
        # Menyimpan objek ke database
        new_product.save()

        # Mengembalikan respons sederhana bahwa data berhasil dibuat
        return HttpResponse(b"CREATED", status=201)
    
    # Jika bukan POST, kembalikan error
    return HttpResponse(status=405)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    instance = get_object_or_404(Product, pk=id)
    # Cek apakah user yang mengedit adalah pemilik produk
    if instance.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'You are not authorized to edit this product.'}, status=403)

    form = ProductForm(request.POST, instance=instance)
    if form.is_valid():
        form.save() # Simpan perubahan
        
        # Kirim kembali data yang sudah diperbarui
        updated_product = {
            'id': str(instance.id),
            'name': instance.name,
            'price': instance.price,
            'category': instance.category,
            'description': instance.description,
            'thumbnail': instance.thumbnail,
            'is_featured': instance.is_featured,

            
        }
        return JsonResponse({'status': 'success', 'product': updated_product})
    else:
        # Jika form tidak valid, kirim errornya
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)