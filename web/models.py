from django.db import models

# Create your models here.



class enquiry(models.Model):
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)
    email = models.EmailField()
    message = models.CharField(max_length = 120)

    def __str__(self):
        return self.fname
      