from django.db import models

# Create your models here.
class Candidate(models.Model):
    title = models.CharField(max_length=100)

class Skill(models.Model):
    title = models.CharField(max_length=100, unique=True)

class Candidate_Skills(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
