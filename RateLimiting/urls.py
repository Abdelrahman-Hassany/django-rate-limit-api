from django.urls import path
from .views import SendMailApiView

urlpatterns = [
    path('send-mail/',SendMailApiView.as_view(),name='api_send_mail')
]