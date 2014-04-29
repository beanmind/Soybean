from django.db import models

class People(models.Model):
    id = models.Charfield(max_length=10)
    name = models.Charfield(max_length=30)
    surname = models.Charfield(max_length=30)
    password = models.Charfield(max_length=32)

    def __unicode__(self):
        return self.prenom + " " + self.nom