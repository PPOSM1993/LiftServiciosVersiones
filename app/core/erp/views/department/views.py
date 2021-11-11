from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import DepartmentForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Department


class DepartmentListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Department
    template_name = 'department/list.html'
    permission_required = 'erp.view_department'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Department.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position+=1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Departamentos'
        context['create_url'] = reverse_lazy('erp:department_create')
        context['list_url'] = reverse_lazy('erp:department_list')
        context['entity'] = 'Departamentos'
        return context


class DepartmentCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/create.html'
    success_url = reverse_lazy('erp:department_list')
    permission_required = 'erp.add_department'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación Departamento'
        context['entity'] = 'Departamentos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class DepartmentUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/create.html'
    success_url = reverse_lazy('erp:department_list')
    permission_required = 'erp.change_department'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición Departamento'
        context['entity'] = 'Departamentos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class DepartmentDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Department
    template_name = 'department/delete.html'
    success_url = reverse_lazy('erp:department_list')
    permission_required = 'erp.delete_department'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación Departamento'
        context['entity'] = 'Departamentos'
        context['list_url'] = self.success_url
        return context
