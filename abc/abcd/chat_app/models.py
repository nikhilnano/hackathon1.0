from django.db import models

# Create your models here.
class chat (models.Model):
	username  =models.CharField(max_length=50,default="enter the valid username")
	message   =models.TextField(default="please enter the text")

