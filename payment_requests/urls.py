from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


payment_request_list = PaymentRequestViewSet.as_view({
    'get': 'table_list'
})

payment_request_detail = PaymentRequestViewSet.as_view({
    'get': 'details',
    'post': 'update'
})

payment_request_create = PaymentRequestViewSet.as_view({
    'get': 'new',
    'post': 'save'

})

app_name = 'payment_requests'
urlpatterns = [
    path('list', payment_request_list, name='pr_main_url'),
    path('<int:pk>', payment_request_detail, name='pr_detail_url'),
    path('new/', payment_request_create, name='pr_create_url'),
    path('upload/', payment_request_detail, name='pr_upload_url')
]

urlpatterns = format_suffix_patterns(urlpatterns)
