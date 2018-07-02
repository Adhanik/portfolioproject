from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()#TextField allows more data to be stored than CharField
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:50]
    def time(self):
        return self.pub_date.strftime('%b %e %Y')
    #def __str__(self):
        #return self.title
