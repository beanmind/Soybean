from django.db import models

class People(models.Model):
    identifier = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    password = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name + " " + self.surname