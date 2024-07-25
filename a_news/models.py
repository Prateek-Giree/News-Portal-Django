from django.db import models

# Create your models here.

from django.db import models


class News(models.Model):
    CATEGORY_CHOICES = [
        ('capital', 'Capital'),
        ('nation', 'Nation'),
        ('politics', 'Politics'),
        ('global', 'Global'),
        ('stock', 'Stock'),
        ('sports', 'Sports'),
        ('science_tech', 'Science & Tech'),
        ('weather', 'Weather'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    image = models.ImageField(null=False, blank=False)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
