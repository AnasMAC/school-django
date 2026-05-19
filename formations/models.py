from django.db import models

class Formation(models.Model):
    formation_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in weeks or months

    def __str__(self):
        return self.formation_name