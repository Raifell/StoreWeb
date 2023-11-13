from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.product_list_page, name='product_list_page'),
    path('product/<slug:p_slug>/', views.product_detail_page, name='product_detail_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
