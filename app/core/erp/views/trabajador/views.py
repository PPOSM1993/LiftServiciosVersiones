from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import TrabajadorForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Trabajador


class TrabajadorListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Trabajador
    template_name = 'trabajador/list.html'
    permission_required = 'erp.view_trabajador'

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
                for i in Trabajador.objects.all():
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
        context['title'] = 'Listado de Trabajadores'
        context['create_url'] = reverse_lazy('erp:trabajador_create')
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        context['entity'] = 'Trabajadores'
        return context


class TrabajadorCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('erp:trabajador_list')
    permission_required = 'erp.add_trabajador'
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
                data['error'] = 'No ha ingresado a ninguna opci??n'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creaci??n de un Trabajador'
        context['entity'] = 'Trabajadores'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TrabajadorUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('erp:trabajador_list')
    permission_required = 'erp.change_trabajador'
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
                data['error'] = 'No ha ingresado a ninguna opci??n'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edici??n de un Trabajador'
        context['entity'] = 'Trabajadores'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TrabajadorDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Trabajador
    template_name = 'trabajador/delete.html'
    success_url = reverse_lazy('erp:trabajador_list')
    permission_required = 'erp.delete_trabajador'
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
        context['title'] = 'Eliminaci??n de un Trabajador'
        context['entity'] = 'Trabajadores'
        context['list_url'] = self.success_url
        return context
