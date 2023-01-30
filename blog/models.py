from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("articles:detail", kwargs={"my_id": self.id})
