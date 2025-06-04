from rest_framework import serializers

class SendMailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)