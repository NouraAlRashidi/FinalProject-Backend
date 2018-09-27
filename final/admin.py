from django.contrib import admin
from .models import Employer, Candidate, Result, Test, Question, Choice

admin.site.register(Employer)
admin.site.register(Candidate)

admin.site.register(Result)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Choice)



# Register your models here.
