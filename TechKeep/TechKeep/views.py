from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Product, Room
from .utils import generate_room_code
import json

def h_f(request):
    user = request.user

def index(request):
    rooms = request.user.rooms.all()

    return render(request, "index.html", {
        "rooms": rooms
    })

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def catalog(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    products = Product.objects.filter(room_id=room_id)
    
    return render(request, "catalog.html", {
        "products": products,
        "room": room
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
@login_required
def create_room(request):
    name = request.POST.get('name')
    user = request.user

    if not name:
        return JsonResponse(
            {'success': False, 'message': 'Название комнаты не может быть пустым'},
            status=400
        )

    code = generate_room_code()
    while Room.objects.filter(code=code).exists():
        code = generate_room_code()

    room = Room.objects.create(name=name, code=code)
    room.users.add(user)

    return redirect('catalog', room_id=room.id)

@require_POST
@login_required
def connect_room(request):
    code = request.POST.get('code')
    user = request.user
    room = Room.objects.filter(code=code).first()

    if (user not in room.users.all()):
        room.users.add(user)

    return redirect('catalog', room_id=room.id)

@require_POST
def add_product(request, room_id):
    type_ = request.POST.get('type', 'other')
    allowed_type = dict(Product.CATEGORY_CHOICES)
    room = Room.Objects.get(id=room_id)

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

    if type_ not in allowed_type:
        return JsonResponse(
            {'success': False, 'message': 'Неверный тип продукта'},
            status=400
        )

    Product.objects.create(
        room=room,
        name=request.POST.get('name'),
        description=request.POST.get('description'),
        type = type_,
        image=request.FILES.get('image'),
    )

    return JsonResponse({'success': True})