from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('apparel', 'Apparel'),
        ('shoes', 'Shoes'),
        ('football', 'Football'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('goalkeeper gear', 'Goalkeeper Gear'),
        ('collectibles', 'Collectibles'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

