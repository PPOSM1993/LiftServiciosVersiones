from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Count
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from core.erp.forms import BuyForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Buy


class BuyCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Buy
    form_class = BuyForm
    template_name = 'buy/create.html'
    success_url = reverse_lazy('index')
    permission_required = 'erp.add_buy'
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
        context['title'] = 'Creación de Compra'
        context['entity'] = 'Compras'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context