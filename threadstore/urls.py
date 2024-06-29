"""
URL configuration for threadstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from store import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("products/<int:pk>/",views.ProductDetailView.as_view(),name="product-detail"),
    path("product/cart/index/add/<int:pk>",views.AddToCartView.as_view(),name="add-to-cart"),
    path("cart/all/",views.CartSummaryView.as_view(),name="cart-summary"),
    path("cart/<int:pk>/delete/",views.CartDestryoyView.as_view(),name="cart-delete"),
    path("signout/",views.SignOutView.as_view(),name="signout"),
    path("cart/update/<int:pk>/",views.CartUpdateQuantityView.as_view(),name="cart-update"),
    path("checkout/cart/",views.PlaceOrderView.as_view(),name="place-order"),
    path("myorders/",views.OrderSummaryView.as_view(),name="myorders"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
