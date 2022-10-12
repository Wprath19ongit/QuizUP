from djongo import models

# Create your models here.

class USER(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    username = models.CharField(max_length = 50, unique=True)
    log_in = models.DateField(max_length = 50)
    reg_time = models.DateField(max_length = 50)
    password = models.CharField(max_length = 50)
