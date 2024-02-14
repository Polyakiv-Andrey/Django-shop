from django.db import models


class SupportRequest(models.Model):
    name = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=False)
    topic = models.CharField(blank=False)
    payload = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    response_send = models.BooleanField(default=False)

    def __str__(self):
        return self.email
