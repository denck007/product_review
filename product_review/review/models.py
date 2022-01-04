from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.utils.text import slugify
from io import BytesIO
import os
from PIL import Image


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="tags", on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"{settings.API_HOST_URL}/tags/{self.slug}"


class Review(models.Model):
    product = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="reviews")
    score = models.PositiveSmallIntegerField(null=False, default=3)

    notes = models.TextField(max_length=4096, blank=True, null=True)
    store = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    product_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="product_images/thumbnails/", blank=True, null=True)

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return f"{self.user} - {self.product} - {self.created_at:%Y-%m-%d}"

    def get_absolute_url(self):
        return f"{settings.API_HOST_URL}/reviews/{self.id}"

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST_URL + self.image.url
        else:
            return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return settings.MEDIA_HOST_URL + self.thumbnail.url
        elif self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return settings.MEDIA_HOST_URL + self.thumbnail.url
        else:
            return ""

    def make_thumbnail(self, image, size=(128, 128)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        thumbnail = File(thumb_io, name=os.path.join("product_images/thumbnails/", os.path.basename(image.name)))

        return thumbnail
