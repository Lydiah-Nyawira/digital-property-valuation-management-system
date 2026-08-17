from django.db import models

class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ("individual", "Individual"),
        ("company", "Company"),
        ("diaspora", "Diaspora"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES, default="individual")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name# Create your models here.