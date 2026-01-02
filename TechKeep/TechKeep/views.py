from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Product
import json

def h_f(request):
    user = request.user

def index(request):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def catalog(request):
    user = request.user
    products = Product.objects.none()
    is_admin = False

    if user.is_authenticated:
        products = Product.objects.filter(user=user)
        is_admin = user.is_superuser

    # products = Product.objects.filter(user_id=user_id)

    # categories = Product.CATEGORY_CHOICES
    
    return render(request, "catalog.html", {
        "categories": Product.CATEGORY_CHOICES,
        "products": products,
        "is_admin": is_admin
    })

@csrf_exempt
@require_POST
def registerUser(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if User.objects.filter(username=username).exists():
        return JsonResponse({"message": "Ник уже занят."}, status=400)

    user = User.objects.create_user(username=username, password=password)

    login(request, user)
    return JsonResponse({"message": "Пользователь создан"}, status=201)

@require_POST
def loginUser(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Login successful"}, status=200)
    else:
        return JsonResponse({"message": "Invalid credentials"}, status=401)

@csrf_exempt 
def logoutUser(request):
    logout(request)
    return JsonResponse({"message": "Logout successful"}, status=200)

@require_POST
def add_product(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {'success': False, 'message': 'Вы не авторизованы'},
            status=401
        )

    if not request.user.is_staff:
        return JsonResponse(
            {'success': False, 'message': 'Нет прав'},
            status=403
        )

    type_ = request.POST.get('type', 'other')

    allowed_type = dict(Product.CATEGORY_CHOICES)

    if type_ not in allowed_type:
        return JsonResponse(
            {'success': False, 'message': 'Неверный тип продукта'},
            status=400
        )

    Product.objects.create(
        user=request.user,
        name=request.POST.get('name'),
        description=request.POST.get('description'),
        type = type_,
        image=request.FILES.get('image'),
    )

    return JsonResponse({'success': True})