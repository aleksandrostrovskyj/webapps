from django.urls import path

from .views import *

app_name = 'payment_requests'
urlpatterns = [
    path('', PaymentRequestList.as_view(), name='pr_main_url'),
    path('<int:pk>', PaymentRequestDetail.as_view(), name='pr_detail_url'),
    path('new/', PaymentRequestCreate.as_view(), name='pr_create_url'),
    path('<int:pk>/edit', PaymentRequestEdit.as_view(), name='pr_edit_url'),
    path('upload/', PaymentRequestUpload.as_view(), name='pr_upload_url')
]
