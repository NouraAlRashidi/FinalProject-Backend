from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Employer(models.Model):
	company_name = models.CharField(max_length=200)
	company_email = models.EmailField(max_length=200)

	def __str__(self):
		return self.company_name


class Candidate(models.Model):
	candidate_email =models.EmailField(max_length=200)
	employers = models.ManyToManyField(Employer, related_name="candidates")

	def __str__(self):
		return self.candidate_email

class Test(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=200)
	candidate_result = models.ManyToManyField(Candidate, through="Result")


class Result(models.Model):
	score = models.CharField(max_length=100)
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	test = models.ForeignKey(Test, on_delete=models.CASCADE)



class Question(models.Model):
	question = models.CharField(max_length=200)
	test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Choice(models.Model):
	choice = models.CharField(max_length=150)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)	


# class CandidateStep (models.Model):
# 	candidate = models.ManyToManyField(Candidate, through )



