from django.db import models


class NewsItem(models.Model):
    date_published = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        ordering = ['-date_published', '-id']

    def __str__(self):
        return f"{self.date_published} - {self.title}"
