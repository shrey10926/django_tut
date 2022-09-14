from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class IrisModel(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    sepal_length = models.DecimalField(max_digits = 6, decimal_places = 6)
    sepal_width = models.DecimalField(max_digits = 6, decimal_places = 6)
    petal_length = models.DecimalField(max_digits = 6, decimal_places = 6)
    petal_width = models.DecimalField(max_digits = 6, decimal_places = 6)
    
    
class PostModel(models.Model):
    
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    date = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    
    def __str__(self):
        
        return self.title
    
    
    def get_absolute_url(self):
        
        return reverse('post-detail', kwargs={'pk' : self.pk})







