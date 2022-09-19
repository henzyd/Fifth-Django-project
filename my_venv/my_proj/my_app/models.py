from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.title}'