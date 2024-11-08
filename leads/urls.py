# from django.urls import path
# from .views import (lead_list, lead_detials, lead_create, lead_update, 
#                     lead_delete, LeadListView, LeadCreateView, LeadDeleteView, LeadDetailView, LeadUpdateView)
       

# app_name = 'leads' 

# urlpatterns = [
#     # path('', lead_list, name='lead-list'),
#     path('', LeadListView.as_view(), name = 'lead-list'),
#     # path('<int:pk>/', lead_detials, name='lead-details'),
#     path('<int:pk>/', LeadDetailView.as_view(), name='lead-details'),
#     # path('create/', lead_create, name='lead-create'),
#     path('create/', LeadCreateView.as_view(), name ='lead-create'),
#     # path('update/<int:pk>/', lead_update, name='lead-update'),
#     path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
#     # path('delete/<int:pk>/', lead_delete, name='lead-delete'),
#     path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
# ]

from django.urls import path
from .views import (
    LeadListView, LeadCreateView, LeadDetailView, LeadUpdateView, LeadDeleteView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-details'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='lead-update'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead-delete'),
]
