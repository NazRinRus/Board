from django.core.mail import send_mail
from .models import Ads, Post, User
from Board import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Post)
def notify_managers_post(sender, instance, created, **kwargs):
    author_post = instance.author_post
    ad = instance.post_at_ad
    if created:
        send_mail(subject=f'Новый отклик',
                  message=f'На Вашу статью "{ad.header}" поступил новый отклик',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[author_post.email, ]
                 )
