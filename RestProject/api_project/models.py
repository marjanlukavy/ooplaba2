from django.db import models
from django.utils import timezone
# Create your models here.
class Dog(models.Model):
    name  =  models.CharField(max_length=100)
    weight = models.IntegerField(null=True)
    owner = models.CharField(max_length=100)
    email  = models.EmailField(max_length=100)
    website = models.URLField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()
