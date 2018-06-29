from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField()#TextField allows more data to be stored than CharField
    image = models.ImageField(upload_to='images/')
