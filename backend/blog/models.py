from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=64, null=False, blank=False)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.title} | {self.created}'
