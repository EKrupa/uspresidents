from django.db import models


# Create your models here.
class Presidents(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default=True)
    number = models.IntegerField()
    image = models.ImageField(upload_to='static', default=True)

    




    def __str__(self):
        return self.name 
 
