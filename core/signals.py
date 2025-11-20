from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Si es el primer usuario creado → admin automático
        if User.objects.count() == 1:
            Profile.objects.create(user=instance, role="admin")
        else:
            Profile.objects.create(user=instance, role="cliente")

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
