from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class Question(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    question_text = models.CharField(max_length=200)
    answer_choices = models.JSONField()
    correct_answer = models.CharField(max_length=200)
    correct_answer2 = models.CharField(max_length=200, blank=True, null=True)
    correct_answer3 = models.CharField(max_length=200, blank=True, null=True)
    correct_answer4 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.question_text

class Participant(models.Model):
    score = models.IntegerField(default=0)
    id = models.CharField(max_length=50, primary_key=True)
    answers = models.JSONField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    
    def save(self, *args, **kwargs):
        # Set the 'id' field of Participant to match the 'id' of the associated User
        self.id = self.user.id
        super(Participant, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Limit(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.count)


@receiver(post_save, sender=Participant)
def update_limit_count(sender, instance, created, **kwargs):
    if instance.score >= 7:
        limit = Limit.objects.first()
        if limit is None:
            limit = Limit.objects.create(count=1)
        else:
            limit.count = Participant.objects.filter(score__gte=7).count()
            limit.save()
            
            
            
class PDF(models.Model):
    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')
    
    def __str__(self):
        return self.name
