from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, View
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PaymentRequest
from .forms import PaymentRequestForm, UploadRequestForm

from .serializers import PaymentRequestSerializer

import io
import csv
from datetime import datetime
# Create your views here.



class PaymentRequestList(APIView):
    serializer_class = PaymentRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment_requests/index.html'

    def get(self, request):
        queryset = PaymentRequest.objects.all()
        columns = [field.label for field in self.serializer_class()]
        data = self.serializer_class(queryset, many=True).data
        table_data = [each.values() for each in data]
        ids_list = [each['id'] for each in data]
        context = {
            'columns': columns,
            'table_data': zip(table_data, ids_list)
        }
        return Response(context)

class PaymentRequestDetail(APIView):
    serializer_class = PaymentRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment_requests/detail.html'

    def get(self, request, pk):
        payment_request = get_object_or_404(PaymentRequest, pk=pk)
        return Response({'serializer': self.serializer_class(payment_request)})

class PaymentRequestEdit(APIView):
    serializer_class = PaymentRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment_requests/edit.html'

    def get(self, request, pk):
        payment_request = get_object_or_404(PaymentRequest, pk=pk)
        return Response({'serializer': self.serializer_class(payment_request)})

    def post(self, request, pk):
        payment_request = get_object_or_404(PaymentRequest, pk=pk)
        serializer = self.serializer_class(payment_request, data=request.data)

        if not serializer.is_valid():
            return Response({'serializer': serializer, 'payment_request': payment_request})

        updated_payment_request = serializer.save()
        return redirect(updated_payment_request)

class PaymentRequestCreate(APIView):
    serializer_class = PaymentRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment_requests/create.html'

    def get(self, request):
        return Response({'serializer': self.serializer_class()})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({'serializer': serializer})

        new_payment_request = serializer.save()
        return redirect(new_payment_request)

class PaymentRequestUpload(APIView):
    serializer_class = PaymentRequestSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payment_requests/upload.html'

# class PaymentRequestList(LoginRequiredMixin, ListView):
#     #TODO - Add pagination
#     paginate_by = 50
#     model = PaymentRequest
#     template_name = 'payment_requests/index.html'
#     context_object_name = 'payment_requests_list'
#     #Define which data should be displayed in table
#     columns_to_display = [
#         'id',
#         'request_date',
#         'department',
#         'subdivision',
#         'user',
#         'currency',
#         'amount',
#         'planned_payment_date',
#         'compositions_of_payment_negotiations',
#         'ceo',
#         'fact_payment_date'
#     ]
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         all_payment_requests = context['payment_requests_list']
#
#         #Choices dict
#         choices_dict = {}
#         [choices_dict.update(dict(field.choices)) for field in self.model._meta.fields if field.choices]
#
#         #Data for table with readable values for choices fields
#         #Contains values only for columns_to_display list
#         table_data = [
#             (choices_dict.get(each, each) for each in row)
#             for row in all_payment_requests.values_list(*self.columns_to_display)
#         ]
#         context['columns'] = [f.verbose_name for f in self.model._meta.fields if f.name in self.columns_to_display]
#         context['table_data'] = zip(table_data, all_payment_requests)
#         return context
#
# class PaymentRequestDetail(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         payment_request = get_object_or_404(PaymentRequest, pk=pk)
#         bound_form = PaymentRequestForm(instance=payment_request)
#         return render(request, 'payment_requests/detail.html', {'form': bound_form, 'payment_request': payment_request})
#
# class PaymentRequestCreate(LoginRequiredMixin, View):
#     def get(self, request):
#         bound_form = PaymentRequestForm()
#         return render(request, 'payment_requests/create.html', {'form': bound_form})
#
#     def post(self, request):
#         bound_form = PaymentRequestForm(request.POST)
#         if bound_form.is_valid():
#             new_payment_request = bound_form.save()
#             return redirect(new_payment_request)
#         return render(request, 'payment_requests/create.html', {'form': bound_form})
#
# class PaymentRequestEdit(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         payment_request = get_object_or_404(PaymentRequest, pk=pk)
#         bound_form = PaymentRequestForm(instance=payment_request)
#         return render(request, 'payment_requests/edit.html', {'form': bound_form, 'payment_request': payment_request})
#
#     def post(self, request, pk):
#         payment_request = get_object_or_404(PaymentRequest, pk=pk)
#         bound_form = PaymentRequestForm(request.POST, instance=payment_request)
#         if bound_form.is_valid():
#             updated_payment_request = bound_form.save()
#             return redirect(updated_payment_request)
#         return render(request, 'payment_requests/edit.html', {'form': bound_form, 'payment_request': payment_request})
#
# class PaymentRequestUpload(LoginRequiredMixin, View):
#
#     def create_pr_from_csv(self, obj):
#
#         def revert_choices_dict(choices_list):
#             return {v:k for k, v in dict(choices_list).items()}
#
#         payment_method_dict = revert_choices_dict(PaymentRequest.PAYMENT_METHOD_CHOICES)
#         payment_system_dict = revert_choices_dict(PaymentRequest.PAYMENT_SYSTEM_CHOICES)
#         payment_currency_dict = revert_choices_dict(PaymentRequest.CURRENCY_CHOICES)
#         data = csv.reader(io.StringIO(obj.read().decode('utf-8', 'ignore')))
#
#         saved_payment_requests = []
#
#         for each in data:
#
#             #TODO - add message for invalid data (choices fields)
#             try:
#                 new_payment_request = PaymentRequest(payment_metod=payment_method_dict[each[0]],
#                                department = each[1],
#                                subdivision = each[2],
#                                 user = each[3],
#                                 payment_system = payment_system_dict[each[4]],
#                                 recipient = each[5],
#                                 requisits = each[6],
#                                 form_w8ben_w9 = each[7],
#                                 payment_details = each[8],
#                                 currency = payment_currency_dict[each[9]],
#                                 amount = each[10],
#                                 planned_payment_date = datetime.strptime(each[11], '%m/%d/%Y').date())
#                 new_payment_request.save()
#                 saved_payment_requests.append(new_payment_request.pk)
#             except Exception:
#                 ...
#
#         return saved_payment_requests
#
#     def get(self, request):
#         bound_form = UploadRequestForm()
#         return render(request, 'payment_requests/upload.html', {'form': bound_form})
#
#     def post(self, request):
#         self.create_pr_from_csv(request.FILES['file_field'])
#         return redirect('/internal_tools/payment_requests/')
