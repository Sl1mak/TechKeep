from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

def h_f(request):
    username = request.session.get('username')

def index(request):
    username = request.session.get('username')
    return render(request, "index.html", {"username": username})

def catalog(request):
    username = request.session.get('username')
    categories = [
        {"title": "Смартфоны"},
        {"title": "Планшеты"},
        {"title": "Ноутбуки"},
        {"title": "Компьютеры"},
        {"title": "Аксессуары"},
        {"title": "Электроника"},
    ]
    return render(request, "catalog.html", {
        "username": username,
        "categories": categories
    })


def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Ник уже занят."}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"message": "Email уже занят."}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        request.session['user_id'] = user.id
        request.session['username'] = user.username

        return JsonResponse({"message": "Пользователь создан"}, status=201)

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"message": "Invalid credentials"}, status=401)

@csrf_exempt 
def logoutUser(request):
    request.session.flush()
    return JsonResponse({"message": "Logout successful"}, status=200)