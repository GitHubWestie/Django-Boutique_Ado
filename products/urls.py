from django.urls import path
# The . tells python to get views from the same directory this urls.py is in
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail')
]