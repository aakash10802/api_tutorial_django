 
from django.urls import path
from .views import PersonView  

urlpatterns = [
      # This handles the root path
    path('items/', PersonView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', PersonView.as_view(), name='item-detail-update-delete'),
]
