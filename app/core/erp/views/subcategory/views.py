from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import SubCategoryForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Subcategory


class SubCategoryListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Subcategory
    template_name = 'subcategory/list.html'
    permission_required = 'erp.view_subcategory'

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
                for i in Subcategory.objects.all():
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
        context['title'] = 'Listado de Subcategorías'
        context['create_url'] = reverse_lazy('erp:subcategory_create')
        context['list_url'] = reverse_lazy('erp:subcategory_list')
        context['entity'] = 'Subcategorias'
        return context


class SubCategoryCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Subcategory
    form_class = SubCategoryForm
    template_name = 'subcategory/create.html'
    success_url = reverse_lazy('erp:subcategory_list')
    permission_required = 'erp.add_subcategory'
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
        context['title'] = 'Creación de una Subcategoria'
        context['entity'] = 'Categorias'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class SubCategoryUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Subcategory
    form_class = SubCategoryForm
    template_name = 'subcategory/create.html'
    success_url = reverse_lazy('erp:subcategory_list')
    permission_required = 'erp.change_subcategory'
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
        context['title'] = 'Edición de una Subcategoria'
        context['entity'] = 'Subcategorias'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class SubCategoryDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Subcategory
    template_name = 'subcategory/delete.html'
    success_url = reverse_lazy('erp:subcategory_list')
    permission_required = 'erp.delete_subcategory'
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
        context['title'] = 'Eliminación de una Subcategoria'
        context['entity'] = 'Subcategorias'
        context['list_url'] = self.success_url
        return context
