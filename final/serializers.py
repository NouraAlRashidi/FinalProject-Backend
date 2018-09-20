from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


class UserCreateSerializer(serializers.ModelSerializer):
	token = serializers.CharField(write_only=True)

	class Meta:
		model = User
		fields = ['password','email','token']

	def create (self, validated_data):
		password = validated_data['password']
		email = validated_data['email']
		
		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload =jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token
        return validated_data 



class EmployerListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employer
		fields = ['company_name', 'company_email']

		