from rest_framework import serializers 
from . import models

class ResponseSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length = 100, allow_blank = True, required = False)
    user_response = serializers.CharField(max_length = 100, allow_blank = True, required = False, default = 'timeout')
    response_image = serializers.CharField(max_length = 100, required = False, allow_blank = True, default = '') 

    def create(self, validated_data):
        return models.UserResponse.objects.create(**validated_data)