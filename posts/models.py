from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User = get_user_model()
class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    question_title = models.CharField(max_length=200, unique=True)
    question_description = models.TextField(blank=False)
    created_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.question_title

    #def get_absolute_url(self):
     #   return reverse('')
   # class Meta:
    #    ordering=['-created_at']