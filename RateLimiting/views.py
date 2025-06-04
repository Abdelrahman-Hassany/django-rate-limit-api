from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import SendMailSerializer
from .utils.ratelimit import sendmail_ratelimit
from .utils.sendmail import send_test_mail
from rest_framework.response import Response
from rest_framework import status
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
class SendMailApiView(APIView):
    serializer_class = SendMailSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        
        if email:
            if sendmail_ratelimit(email):
                if send_test_mail(email):
                    return Response({'message':'Send mail Sucess'},status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Failed to send email due to server issue'})
            return Response({'message':'You send too many requests, u blocked temporary'},status=status.HTTP_429_TOO_MANY_REQUESTS)
                    