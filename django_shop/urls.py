"""
URL configuration for django_shop project.

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import HomePageView
from django_shop import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_panel/', include("admin_panel.urls", namespace="admin-panel")),
    path('catalog/', include("catalog.urls", namespace="catalog")),
    path('products/', include("products.urls", namespace="products")),
    path('basket/', include("basket.urls", namespace="basket")),
    path('delivery/', include("logistic.urls", namespace="logistic")),
    path('payment/', include("payment.urls", namespace="payment")),
    path('orders/', include("orders.urls", namespace="orders")),
    path('reviews/', include("reviews.urls", namespace="reviews")),
    path('about-us/', include("site_detail.urls", namespace="site_detail")),
    path("contact-us-request-form/", include("support.urls", namespace="support")),
    path('', HomePageView.as_view(), name="home"),
] + static(
    settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

