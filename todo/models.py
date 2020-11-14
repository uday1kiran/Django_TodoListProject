from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	title = models.CharFiled(max_lenght=100)
	memo = models.TextField(blank=True)
	created=models.DateTimeField(auto_now_add=True)
	datecompleted=moels.DateTimeField(null=True, blank=True)
	important=models.BooelanField(default=False)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
