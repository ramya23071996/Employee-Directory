# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Department
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class EmployeeListView(ListView):
    model = Employee
    template_name = 'directory/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        department = self.request.GET.get('department')
        if department:
            return Employee.objects.filter(department__name=department)
        return Employee.objects.all()

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'directory/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = f"Department > {self.object.department.name} > {self.object.name}"
        return context

class HRPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class EmployeeCreateView(HRPermissionMixin, CreateView):
    model = Employee
    fields = ['name', 'email', 'phone', 'department', 'position']
    template_name = 'directory/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(HRPermissionMixin, UpdateView):
    model = Employee
    fields = ['name', 'email', 'phone', 'department', 'position']
    template_name = 'directory/employee_form.html'
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(HRPermissionMixin, DeleteView):
    model = Employee
    template_name = 'directory/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')
