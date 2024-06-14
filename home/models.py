# models.py
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    button_text = models.CharField(max_length=50)
    next_question = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text
