from django.db import models
# Create your models here.
class Riddle(models.Model):   # будет содержаться загадка
    riddle_text = models.CharField(max_length=255)   #max_length=255
    pub_date = models.DateTimeField('date published')


class Option(models.Model):    # один из возможных ответов на загадку
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=3555)   #max_length=255
    correct = models.BooleanField(default=False)
