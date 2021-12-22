from django.db import models

# Create your models here.
class Resturant(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    story = models.TextField()
    quote_text = models.TextField()
    quote_by = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about_us = models.TextField()
    facebook_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    address = models.TextField()
    alternate_phone = models.CharField(max_length=100)
    closed_on = models.CharField(max_length=100)
    mon_sat_time = models.CharField(max_length=100)
    sun_time = models.CharField(max_length=100)
    review_quote = models.TextField()
    review_quote_by = models.CharField(max_length=100)
    menu_quote = models.TextField()
    item_currency_symbol = models.CharField(max_length=100)
    gallery_quote = models.TextField()
    contact_quote = models.TextField()
    reservation_quote = models.TextField()
    copyright_year = models.CharField(max_length=100)
    designed_by_url = models.CharField(max_length=100)
    designed_by_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pics')

class Reviews(models.Model):
    review_text = models.TextField()
    reviewer_job = models.CharField(max_length=100)
    reviewer_name = models.CharField(max_length=100)

class Subscriber(models.Model):
    email = models.CharField(max_length=100)

class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_category = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to='pics')

class Gallery(models.Model):
    image = models.ImageField(upload_to='pics')

class Contact_forum(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message =  models.TextField()

class Reservation_forum(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)