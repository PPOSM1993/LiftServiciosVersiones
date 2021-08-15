from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from core.erp.forms import MarcaForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Marca


class MarcaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Marca
    template_name = 'marca/list.html'
    permission_required = 'erp.view_marca'

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
                for i in Marca.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Marcas'
        context['create_url'] = reverse_lazy('erp:marca_create')
        context['list_url'] = reverse_lazy('erp:marca_list')
        context['entity'] = 'Marcas'
        return context


class MarcaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'marca/create.html'
    success_url = reverse_lazy('erp:marca_list')
    permission_required = 'erp.add_marca'
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
        context['title'] = 'Creación de una Marca'
        context['entity'] = 'Marcas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class MarcaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Marca
    form_class = Marca
    template_name = 'marca/create.html'
    success_url = reverse_lazy('erp:marca_list')
    permission_required = 'erp.change_marca'
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
        context['title'] = 'Edición de una Marca'
        context['entity'] = 'Marcas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class MarcaDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Marca
    template_name = 'marca/delete.html'
    success_url = reverse_lazy('erp:marca_list')
    permission_required = 'erp.marca_brand'
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
        context['title'] = 'Eliminación de una Marca'
        context['entity'] = 'Marcas'
        context['list_url'] = self.success_url
        return context
