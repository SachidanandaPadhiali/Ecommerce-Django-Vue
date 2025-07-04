"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import RegisterView
from cart.views import CartView

from django.conf import settings
from django.conf.urls.static import static

# Create a router and register our viewset
router = DefaultRouter()
#router.register('products', ProductViewSet)
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Product API routes
    path('api/', include(router.urls)),
    
    # Endpoint for token authentication (login)
    path('api-token-auth/', obtain_auth_token),
    
    # Endpoint for user registration
    path('api/register/', RegisterView.as_view(), name='register'),
    
    # Endpoint for Cart
    path('cart/', views.get_cart, name='get_cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
