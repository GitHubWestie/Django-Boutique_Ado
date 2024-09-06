from django.urls import path
# The . tells python to get views from the same directory this urls.py is in
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove_from_bag/<item_id>/', views.remove_from_bag, name="remove_from_bag"),
]