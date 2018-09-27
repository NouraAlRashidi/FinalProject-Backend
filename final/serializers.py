from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Test, Question, Choice, Result
from rest_framework.authtoken.models import Token



# class UserCreateSerializer(serializers.ModelSerializer):
# 	token = serializers.CharField(write_only=True)

# 	class Meta:
# 		model = User
# 		fields = ['username','candidate_email','token']

# 	def create (self, validated_data):
# 		candidate_email = validated_data['candidate_email']
# 		username = username ['u']
# 		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# 		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# 		new_user = User(candidate_email=candidate_email)
# 		payload =jwt_payload_handler(new_user)
# 		token = jwt_encode_handler(payload)
# 		validated_data["token"] = token
# 		new_user.save()

# 		return validated_data 



class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ['choice1', 'choice2', 'choice3']


class QuestionSerializer(serializers.ModelSerializer):
	choices = serializers.SerializerMethodField()
	class Meta:
		model = Question
		fields = ['question']

	def get_choices(self,obj):
		choices = obj.choices_set.all()
		return ChoiceSerializer(choices, many=True).data

class TestSerializer(serializers.ModelSerializer):
	questions = serializers.SerializerMethodField()
	class Meta:
		model = Test
		fields = ['title', 'description','questions']

	def get_questions(self,obj):
		questions = obj.question_set.all()
		return QuestionSerializer(questions, many=True).data






class ResultSerializer(serializers.ModelSerializer):
	tests = serializers.SerializerMethodField()
	class Meta:
		model = Result

	def get_test(self,obj):
		request = self.context.get('request')
		tests = obj.test_set.all()

		return TestSerializer(tests, many=True).data




		