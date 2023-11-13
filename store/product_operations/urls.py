from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.product_create_view, name='product_create_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
