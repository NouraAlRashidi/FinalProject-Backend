from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Candidate(models.Model):
	email = models.EmailField(max_length=200, **options)

	def __str__(self):
		return self.email


class Employer(models.Model):
	company_name = models.CharField(max_length=200)
	company_email = models.EmailField(max_length=200, **options)

	def __str__(self):
		return self.company_name


# class CandidateStep (models.Model):
# 	candidate = models.ManyToManyField(Candidate, through )



