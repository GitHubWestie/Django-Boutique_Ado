from django.urls import path
# The . tells python to get views from the same directory this urls.py is in
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('add/', views.add_products, name='add_products'),
    path('edit/<int:product_id>/', views.edit_products, name='edit_products'),
    path('delete/<int:product_id>/', views.delete_products, name='delete_products'),
]