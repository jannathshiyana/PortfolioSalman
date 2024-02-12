from django.db import models
from django.urls import reverse


class Icon(models.Model):
    name = models.CharField(max_length=60)
    icon = models.FileField(upload_to='icons')

class Profile(models.Model):
    name = models.CharField(max_length=60)
    profile = models.FileField(upload_to='profiles')

class Portfolio(models.Model):
    INTERIOR = 'interior'
    EXTERIOR = 'exterior'
    CATEGORY_CHOICES = [
        (INTERIOR, 'Interior'),
        (EXTERIOR, 'Exterior'),
        ]
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='portfolios')
    img2 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img3 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img4 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img5 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img6 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img7 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img8 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img9 = models.ImageField(upload_to='portfolios', blank=True, null=True)
    img10 = models.ImageField(upload_to='portfolios', blank=True, null=True)

    description = models.TextField()
    client = models.CharField(max_length=100)
    project_date = models.DateField()

    def get_absolute_url(self):
        return reverse("portfolio-create")
    

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    testimony = models.TextField()
    picture = models.ImageField(upload_to='testimonies', blank=True)

    def get_absolute_url(self):
        return reverse("gallery")
    

