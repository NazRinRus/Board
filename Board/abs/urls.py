from django.urls import path, include
from .views import *


urlpatterns = [
   path('', AdsList.as_view(), name='ads_all'),
   path('<int:pk>/', AdDetail.as_view(), name='ad_id'),
   path('create/', AdCreate.as_view(), name='ad_create'),
   path('<int>/create/', PostCreate.as_view(), name='post_create'),

   path('about/', about, name='about'),
   path('contact/', contact, name='contact'),
]