from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field



class Ads(models.Model):

    class Meta:
        db_table = 'ads'
        verbose_name = 'Ads'
        verbose_name_plural = 'Ad'

    POSITIONS = [
        ['TK', 'Tanks'],
        ['HL', 'Heals'],
        ['DD', 'Damage Dealers'],
        ['MH', 'Merchants'],
        ['GM', 'Guildmasters'],
        ['QG', 'Questgivers'],
        ['BS', 'Blacksmiths'],
        ['LW', 'Leatherworkers'],
        ['PO', 'Potions'],
        ['SM', 'Spell masters'],
    ]

    author_ads = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default='TK')
    text_ads = CKEditor5Field(verbose_name='Текст объявления', config_name='extends')
    time_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.header.title()}: {self.author_ads}'

    def get_absolute_url(self):
        return reverse('ad_id', args=[str(self.id)])

class Post(models.Model):

    class Meta:
        db_table = 'post'
        verbose_name = 'Posts'
        verbose_name_plural = 'Post'

    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
    text_post = models.TextField()
    post_at_ad = models.ForeignKey(Ads, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    respond = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('ad_id', args=[str(self.post_at_ad.pk)])

    def respond_method(self):
        self.respond = True
        self.save()


