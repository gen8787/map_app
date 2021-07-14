from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# ---- T O U R


class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('one_tour', args=[str(self.id)])


# ---- L E G
class Leg(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='legs'
    )
    description = models.CharField(max_length=140)
    distance = models.PositiveIntegerField(null=True, blank=True)
    vertical = models.PositiveIntegerField(null=True, blank=True)
    rate = models.PositiveIntegerField(null=True, blank=True)
    time = models.PositiveIntegerField(null=True, blank=True)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('all_tours')
