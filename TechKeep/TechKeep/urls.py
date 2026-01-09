"""
URL configuration for TechKeep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TechKeep import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.index, name='index'),
    path("catalog/<int:room_id>", views.catalog, name='catalog'),
    path("login", views.login_page, name='login'),
    path("register_page", views.register_page, name='register_page'),

    path("registerUser", views.registerUser, name='registerUser'),
    path("loginUser", views.loginUser, name='loginUser'),
    path("logoutUser", views.logoutUser, name='logoutUser'),
    path("add_product/<int:room_id>/", views.add_product, name='add_product'),
    path("create_room/", views.create_room, name='create_room'),
    path("connect_room/", views.connect_room, name='connect_room'),
    path("delete_product/<int:product_id>/", views.delete_product, name='delete_product'),
    path("exit_room/<int:room_id>/", views.exit_room, name='exit_room'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
