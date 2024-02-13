from django.db import models


class SiteDetail(models.Model):
    class Currency:
        UAN = "uan"
        USD = "usd"
        EURO = "euro"

    CURRENCY_CHOICE = (
        (Currency.UAN, "₴"),
        (Currency.USD, "$"),
        (Currency.EURO, "€")
    )

    site_name = models.CharField(blank=True, null=True)
    logo = models.ImageField(upload_to='site_image/', blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, default=Currency.USD, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    stripe_private_key = models.CharField(max_length=400, blank=True, null=True)
    stripe_public_key = models.CharField(max_length=400, blank=True, null=True)
    about_us_title = models.CharField(blank=True, null=True)
    about_us_description = models.TextField(blank=True, null=True)
    about_us_image = models.ImageField(upload_to='site_image/', blank=True, null=True)

    def __str__(self):
        return self.site_name