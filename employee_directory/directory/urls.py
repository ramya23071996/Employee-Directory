from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee-edit'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
]
