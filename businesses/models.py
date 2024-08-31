from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=None, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=None, blank=True, null=True)
    street_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    city = models.CharField(max_length=255, default=None, blank=True, null=True)
    state = models.CharField(max_length=2, default=None, blank=True, null=True)
    zip_code = models.CharField(max_length=10, default=None, blank=True, null=True)
    product_listing_url = models.URLField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return self.name