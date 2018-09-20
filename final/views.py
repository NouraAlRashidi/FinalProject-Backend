from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer
from .models import Candidate, Employer
from django.hhtp import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import redirect

# Create your views here.

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

	def perform_create(self, serializer):
		serializer.save(company_name = self.request.user)

class EmployerListAPIView(APIView):

	def get(self, request, *args, **kwargs):
		employer_list = Employer.objects.all()
		json_employer_list = EmployerListSerializer(employer_list, many=True, context={"request":request}).data
		return Response(json_employer_list)

