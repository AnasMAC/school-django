from django.db import models
from django.contrib.auth.models import User
from formations.models import Formation

class StudentProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    formation = models.ForeignKey(
        Formation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username