from django.db import models

# Create your models here.


from django.db import models

class Twitter(models.Model):
    timestamp = models.CharField(max_length=128)
    tweets = models.CharField(max_length=128)
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.tweets










