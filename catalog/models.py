from django.db import models


class CatalogItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='catalog/images', null=True, blank=True)
    icon = models.ImageField(upload_to='catalog/icons', null=True, blank=True)

    def __str__(self):
        return self.name
