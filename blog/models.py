from django.db import models

class post(models.Model):

    title = models.CharField(max_length=100)

    def _str_(self):
        return self.title 
