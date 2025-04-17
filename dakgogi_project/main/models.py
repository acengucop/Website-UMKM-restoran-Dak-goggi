from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    Bonus = models.CharField(max_length=100)  # misalnya: "+ FREE 1 RICEBOWL"
    description = models.TextField(blank=True)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='menu/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Promo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='promo/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class MiniItem(models.Model):
    TYPE_CHOICES = [
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=20)
    image = models.ImageField(upload_to='mini/')
    item_type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.item_type})"

from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    stars = models.PositiveIntegerField(default=5)  # Maks 5
    photo = models.ImageField(upload_to='testimonial_photos/', blank=True)

    def __str__(self):
        return self.name
