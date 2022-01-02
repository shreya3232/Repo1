from django.db import models

# Create your models here.

class Questions (models.Model):
    questions_id=models.IntegerField(max_length=3)
    question=models.CharField(max_length=500)
    def __str__(self) :
        return self.question()
