from django.db import models

# Create your models here.

class Question(models.Model):
    the_question = models.CharField(max_length=1000)
    published_at  = models.DateTimeField('date published')

    def __str__(self):
        return self.the_question

class Choice(models.Model): 
    Q = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.CharField(max_length=1000)
    votes  = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
