from .models import incometax
from rest_framework import serializers

class incometaxSerializers(serializers.ModelSerializer):
    class Meta:
        model=incometax
        fields=['income','age']