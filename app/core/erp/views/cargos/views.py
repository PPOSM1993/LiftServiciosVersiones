from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import CargoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Cargos


class CargosListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Cargos
    template_name = 'cargos/list.html'
    permission_required = 'erp.view_cargos'

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
                for i in Cargos.objects.all():
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
        context['title'] = 'Listado de Cargos'
        context['create_url'] = reverse_lazy('erp:cargos_create')
        context['list_url'] = reverse_lazy('erp:cargos_list')
        context['entity'] = 'Cargos'
        return context


class CargosCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Cargos
    form_class = CargoForm
    template_name = 'cargos/create.html'
    success_url = reverse_lazy('erp:cargos_list')
    permission_required = 'erp.add_cargos'
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
        context['title'] = 'Creación Cargos'
        context['entity'] = 'Cargos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class CargosUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Cargos
    form_class = CargoForm
    template_name = 'cargos/create.html'
    success_url = reverse_lazy('erp:cargos_list')
    permission_required = 'erp.change_cargos'
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
        context['title'] = 'Edición Cargos'
        context['entity'] = 'Cargos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class CargosDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Cargos
    template_name = 'cargos/delete.html'
    success_url = reverse_lazy('erp:cargos_list')
    permission_required = 'erp.delete_cargos'
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
        context['title'] = 'Eliminación Cargos'
        context['entity'] = 'Cargos'
        context['list_url'] = self.success_url
        return context
