from django.db import models


class Kat(models.Model):
    name = models.CharField(
        help_text="The name of the kat",
        max_length=255,
    )
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} : {self.age}"
