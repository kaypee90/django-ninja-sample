from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=90)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name