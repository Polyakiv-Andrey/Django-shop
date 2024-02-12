import datetime

from django.db import models
from django.utils import timezone

from catalog.models import CatalogItem


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    catalog_item = models.ForeignKey(CatalogItem, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def is_top(self):
        marks = []
        reviews = self.reviews.all()
        for review in reviews:
            if review.rating:
                marks.append(review.rating)
        if len(marks) == 0:
            return False
        if sum(marks) / len(marks) >= 4:
            return True
        return False


    @property
    def has_comments(self):
        reviews = self.reviews.all()
        for review in reviews:
            if review.comment:
                return True
        return False

    @property
    def has_discount(self):
        discounts = self.discounts.all()
        if discounts:
            for discount in discounts:
                if discount.start_date < timezone.now() < discount.end_date:
                    return True
        return False


    @property
    def get_discount_price(self):
        discounts = self.discounts.all()
        list_discounts = []
        for discount in discounts:
            if discount.start_date <= timezone.now() <= discount.end_date:
                list_discounts.append(discount.percentage)
        if not list_discounts:
            return None
        max_discount = max(list_discounts)
        return float(self.price) * (100 - max_discount) // 100

    @property
    def get_discount(self):
        discounts = self.discounts.all()
        list_discounts = []
        for discount in discounts:
            if discount.start_date <= timezone.now() <= discount.end_date:
                list_discounts.append(discount.percentage)
        if not list_discounts:
            return None
        return int(max(list_discounts))

    @property
    def get_comments_height(self):
        return self.attributes.all().count() * 40

    @property
    def get_discount_end_date(self):
        discount = self.discounts.all().first()
        if discount:
            return discount.end_date.strftime('%Y-%m-%d') if discount.end_date else None
        return None

    @property
    def get_discount_start_date(self):
        discount = self.discounts.all().first()
        if discount:
            return discount.start_date.strftime('%Y-%m-%d') if discount.start_date else None
        return None


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    title = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.value}"

    class Meta:
        ordering = ['id']


def default_end_date():
    return datetime.datetime(9999, 1, 30)


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    percentage = models.FloatField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=default_end_date)

    def __str__(self):
        return self.percentage


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    color = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    main = models.BooleanField(default=False)

    def __str__(self):
        return self.image.url

    class Meta:
        ordering = ['-main', 'id']

