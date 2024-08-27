from django.urls import path
# The . tells python to get views from the same directory this urls.py is in
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag')
]