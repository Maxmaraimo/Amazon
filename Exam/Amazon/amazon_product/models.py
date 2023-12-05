import os
from datetime import datetime

from django.contrib.auth.models import User
from django.db import IntegrityError, models
from smtplib import SMTPException


from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings




class ProductManager(models.Manager):
    pass


class NullPriceException(Exception):
    pass


class Product(models.Model):
    title: str = models.CharField(max_length=50)
    description: str = models.TextField()
    author: User = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    genre: str = models.CharField(max_length=25)
    is_available: bool = models.BooleanField(default=True)
    price: float = models.DecimalField(max_digits=5, decimal_places=2)
    created: datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        default='product_photo/aee977ce-f946-4451-8b9e-bba278ba5f13.png', upload_to="product_photo")

    objects = models.Manager()  # default
    c_objects = ProductManager()  # custom manager

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.genre == None or self.genre == "":
            raise IntegrityError("Type product can't be null")
        if self.price == 0:
            raise NullPriceException
        super().save(*args, **kwargs)

        # We have to save the form first before getting the image path
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def delete(self, *args, **kwargs):
        image_url = self.image.url
        if image_url != '/media/product_photo/aee977ce-f946-4451-8b9e-bba278ba5f13.png':
            os.remove(self.image.path)
        super().delete(*args, **kwargs)



