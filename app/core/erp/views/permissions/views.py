from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import GroupPermissionForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Group


class GroupListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Group
    template_name = 'group/list.html'
    permission_required = 'erp.view_group'

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
                for i in Group.objects.all():
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
        context['title'] = 'Listado de Grupos'
        context['create_url'] = reverse_lazy('erp:group_create')
        context['list_url'] = reverse_lazy('erp:group_list')
        context['entity'] = 'Grupos'
        return context


class GroupCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Group
    form_class = GroupPermissionForm
    template_name = 'group/create.html'
    success_url = reverse_lazy('erp:group_list')
    permission_required = 'erp.add_group'
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
        context['title'] = 'Creación de un Grupo'
        context['entity'] = 'Grupos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class GroupUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Group
    form_class = GroupPermissionForm
    template_name = 'group/create.html'
    success_url = reverse_lazy('erp:group_list')
    permission_required = 'erp.change_group'
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
        context['title'] = 'Edición de un Grupo'
        context['entity'] = 'Grupos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class GroupDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Group
    template_name = 'group/delete.html'
    success_url = reverse_lazy('erp:group_list')
    permission_required = 'erp.delete_group'
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
        context['title'] = 'Eliminación de un Grupo'
        context['entity'] = 'Grupos'
        context['list_url'] = self.success_url
        return context
