from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import  TestSerializer
from .models import Candidate, Employer, Test
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User






# Create your views here.

class TestCreateView(ListAPIView):
	queryset = Test.objects.all()
	serializer_class = TestSerializer



class CandidateCreateView(APIView):
	permission_classes = (AllowAny,)


	def post (self, request, *args, **kwargs):
		# candidate_email = settings.EMAIL_HOST_USER
		# company_email = settings.EMAIL_HOST_USER
		# company_name = settings.EMAIL_HOST_USER

		candidate_email = request.data.get('candidateEmail')
		company_email = request.data.get('companyEmail')
		company_name = request.data.get('companyName')
		
		new_employer = Employer.objects.create(company_email = company_email, company_name= company_name)
		new_candidate = Candidate.objects.create(candidate_email=candidate_email)

		new_candidate.employers.add(new_employer)

		# candidate_email = request.data['candidate_email']
		# company_email= request.data['company_email']
		# company_name = request.data['company_name']
		# username = request.data['candidate_email']

		new_user_candidate, created = User.objects.get_or_create(username=company_email)
		new_user_candidate.set_password(company_email)

		new_user_employer, created2 = User.objects.get_or_create(username=candidate_email)
		new_user_employer.set_password(candidate_email)

		new_user_candidate.save()
		new_user_employer.save()


		token = Token.objects.get_or_create(user=new_user_candidate)

		subject = 'Thank you for registering to our site'
		message = 'it  means the world to us, http://127.0.0.1:8000/url/%s'%(token[0].key)
		email_from = company_email
		recipient_list = [candidate_email]
		send_mail( subject, message, email_from, recipient_list )

		# send_mail(
	 #      'Candidate Assessment',
	 #      'Congratulations! You have been selected to undertake an assessment!',
	 #      company_email,
	 #      [candidate_email],
	 #      'Click on the url below to start your assessment'
	 #      'http://127.0.0.1:8000/url/{{token}}',
	 #      fail_silently = True,
		#   )


		# return Response()
		pass

# what works:
# candidate_email = request.data.get('candidate_email')
#         company_email = request.data.get('company_email')
#         company_name = request.data.get('company_name')
		
#         new_employer = Employer.objects.create(company_email = company_email, company_name= company_name)
#         new_candidate = Candidate.objects.create(candidate_email=candidate_email)

#         new_candidate.employers.add(new_employer)

#         new_user_candidate, created = User.objects.get_or_create(username=company_email)
#         new_user_candidate.set_password(company_email)

#         new_user_employer, created2 = User.objects.get_or_create(username=candidate_email)
#         new_user_employer.set_password(candidate_email)

#         new_user_candidate.save()
#         new_user_employer.save()


#         token = Token.objects.get_or_create(user=new_user_candidate)

#         subject = 'Thank you for registering to our site'
#         message = 'it  means a world to us'
#         email_from = company_email
#         recipient_list = [candidate_email]
#         send_mail( subject, message, email_from, recipient_list )



 


class ResultCreateView(APIView):
	def post(self, request):
		candidate_result = request.candidate_result
		score = Result.objects.create(score=candidate_result)
		return JsonResponse({'Message': "Here is your result", "id": test.id})




