from django.urls import path
# The . tells python to get views from the same directory this urls.py is in
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/', views.edit_products, name='edit_products'),
    path('delete/', views.delete_products, name='delete_products'),
]