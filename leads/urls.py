from django.urls import path
from .views import lead_list, lead_detials, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('<int:pk>/', lead_detials, name='lead-details'),
    path('create/', lead_create, name='lead-create'),
    path('update/<int:pk>/', lead_update, name='lead-update'),
    path('delete/<int:pk>/', lead_delete, name='lead-delete')
]