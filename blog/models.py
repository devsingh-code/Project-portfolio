from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body=models.TextField()


    def __str__(self):
        return self.title



    def summary(self):
        return self.body[0:100]
