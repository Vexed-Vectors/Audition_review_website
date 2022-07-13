from django.db import models
from django.contrib.auth.models import User,auth



class Question(models.Model):
    
    question_text= models.CharField(max_length=500)
    question_text_response= models.CharField(max_length=1000, blank= True)
    INTERESTED_FIELD_CHOICES =[
        ('CONTENT','Content Team' ),
        ('WEBD', 'Web Development'),
        ('VIDEO', 'Video Editing'),
        ('GD', 'Graphic Designing'),
    ]
    
    
    

    def __str__(self):
        return self.question_text
class Choice_Question(models.Model):
    INTERESTED_FIELD_CHOICES =[
        ('CONTENT','Content Team' ),
        ('WEBD', 'Web Development'),
        ('VIDEO', 'Video Editing'),
        ('GD', 'Graphic Designing'),
    ]

    question_text= models.CharField(max_length=500)
    question_text_response= models.CharField(max_length=10, blank= True, choices= INTERESTED_FIELD_CHOICES)



    

# Create your models here.
