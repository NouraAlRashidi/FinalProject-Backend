from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer, TestSerializer
from .models import Candidate, Employer, Test
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.

class TestCreateView(ListAPIView):
	queryset = Test.objects.all()
	serializer_class = TestSerializer



class CandidateCreateView(APIView):

	def post(self, request):
		candidate_email = request.candidate_email
		employer_name = request.employer_name
		company_name = request.company_name
		
		new_employer = Employer.objects.create(employer_name = employer_name, company_name= company_name)
		new_candidate = Candidate.objects.create(candidate_email=candidate_email)

		new_candidate.employer.add(new_employer)

		candidate_email = validated_data['candidate_email']
		username = validated_data ['candidate_email']
		password = validated_data ['candidate_email']
		new_user = User(username=candidate_email)
		new_user.save()


		token = Token.objects.get_or_create(username=candidate_email)
		return token


class ResultCreateView(APIView):
	def post(self, request):
		candidate_result = request.candidate_result
		score = Result.objects.create(score=candidate_result)
		return JsonResponse({'Message': "Here is your result", "id": test.id})




