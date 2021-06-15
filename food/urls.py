from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path('', views.index, name="index"),
    path('items', views.item, name="item"),
    path('<int:item_id>/', views.item_details, name="item_details"),
    path('add-item', views.add_item, name="add_item"),
]
