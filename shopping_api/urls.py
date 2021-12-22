from django.urls import path, include
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('create/', ProductListView.as_view(), name='create'),
    path('update/<pk>', ProductDetailView.as_view(), name='update'),


]
