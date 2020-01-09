from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

from .models import PaymentRequest
from .serializers import PaymentRequestSerializer

# Create your views here.

class PaymentRequestViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = PaymentRequestSerializer
    queryset = PaymentRequest.objects.all()
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    #is @action needed?
    def table_list(self, request, *args, **kwargs):
        template_name='payment_requests/index.html'
        queryset = self.filter_queryset(self.get_queryset())
        columns = [field.label for field in self.get_serializer()]
        page = self.paginate_queryset(queryset)

        if page:
            paginator = super().paginator
            serializer = self.get_serializer(page, many=True)
            table_data = [each.values() for each in serializer.data]
            ids_list = [each['id'] for each in serializer.data]
            context = {
                'columns': columns,
                'table_data': zip(table_data, ids_list),
                'paginator': paginator.get_html_context()
            }

            return Response(context, template_name=template_name)

        serializer = self.get_serializer(queryset, many=True)
        table_data = [each.values() for each in serializer.data]
        ids_list = [each['id'] for each in serializer.data]
        context = {
            'columns': columns,
            'table_data': zip(table_data, ids_list)
        }
        return Response(context, template_name=template_name)

    def details(self, request, *args, **kwargs):
        template_name='payment_requests/detail.html'
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'serializer': serializer}, template_name=template_name)

    def update(self, request, *args, **kwargs):
        template_name='payment_requests/detail.html'
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'serializer': serializer}, template_name=template_name)

    def new(self, request, *args, **kwargs):
        template_name='payment_requests/create.html'
        serializer = self.get_serializer()
        return Response({'serializer': serializer}, template_name=template_name)

    def save(self, request, *args, **kwargs):
        template_name='payment_requests/create.html'
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'serializer': serializer}, template_name=template_name)
