from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.product_create_view, name='product_create_page'),
    path('delete/<slug:p_slug>/', views.product_delete, name='product_delete_page'),
    path('update/<slug:p_slug>/', views.product_update, name='product_update_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
