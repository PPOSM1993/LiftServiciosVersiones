import json
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from xhtml2pdf import pisa

from core.erp.forms import *
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import *

class BuyListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Buy
    template_name = 'buy/list.html'
    permission_required = 'erp.view_buy'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Buy.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetBuy.objects.filter(buy_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Compras'
        context['create_url'] = reverse_lazy('erp:buy_create')
        context['list_url'] = reverse_lazy('erp:buy_list')
        context['entity'] = 'Compras'
        return context


class BuyCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Buy
    form_class = BuyForm
    template_name = 'buy/create.html'
    success_url = reverse_lazy('erp:buy_list')
    permission_required = 'erp.add_buy'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    #item['value'] = i.name
                    item['text'] = i.name
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    comps = json.loads(request.POST['comps'])
                    buy = Buy()
                    buy.date_joined = comps['date_joined']
                    buy.prove_id = comps['prove']
                    buy.subtotal = float(comps['subtotal'])
                    buy.total = float(comps['total'])
                    buy.save()
                    for i in comps['products']:
                        det = DetBuy()
                        det.buy_id = buy.id
                        det.prod_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['preciocompra'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
            elif action == 'search_proveedor':
                data = []
                term = request.POST['term']
                proveedor = Proveedor.objects.filter(
                    Q(names__icontains=term) | Q(rut__icontains=term))[0:10]
                for i in proveedor:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de Compra'
        context['entity'] = 'Compra'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        return context

class BuyUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Buy
    form_class = BuyForm
    template_name = 'buy/create.html'
    success_url = reverse_lazy('erp:buy_list')
    permission_required = 'erp.change_buy'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            elif action == 'edit':
                with transaction.atomic():
                    comps = json.loads(request.POST['comps'])
                    buy = self.get_object()
                    buy.date_joined = comps['date_joined']
                    buy.prove_id = comps['prove']
                    buy.subtotal = float(comps['subtotal'])
                    buy.total = float(comps['total'])
                    buy.save()
                    buy.detbuy_set.all().delete()
                    for i in comps['products']:
                        det = DetBuy()
                        det.buy_id = buy.id
                        det.prod_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['preciocompra'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
            elif action == 'search_proveedor':
                data = []
                term = request.POST['term']
                proveedor = Proveedor.objects.filter(
                    Q(names__icontains=term) | Q(rut__icontains=term))[0:10]
                for i in proveedor:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_details_product(self):
        data = []
        try:
            for i in DetBuy.objects.filter(buy_id=self.get_object().id):
                item = i.prod.toJSON()
                item['cant'] = i.cant
                data.append(item)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición Compra'
        context['entity'] = 'Compras'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['det'] = json.dumps(self.get_details_product())
        return context


class BuyDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Buy
    template_name = 'buy/delete.html'
    success_url = reverse_lazy('erp:buy_list')
    permission_required = 'erp.delete_buy'
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
        context['title'] = 'Eliminación de Compra'
        context['entity'] = 'Compras'
        context['list_url'] = self.success_url
        return context


class BuyExpensesPDFView(View):
    def get(self,request, *args, **kwargs):
        template = get_template('buy/expenses.html')
        context = {'title': 'Wena cochino culiao xD'}
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        
        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
