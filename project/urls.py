"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('singup/',views.singup),
    path('login/',views.login),
    path('product/<id>/',views.proddisplay,name='dispaly'),
    path('cart/<id>/',views.cartadd,name='cart'),
    path('cartdisplay/',views.cartdisplay),
    path('category/<id>/',views.categorie,name='category'),
    path('account/',views.account),
    path('contact/',views.contact),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
