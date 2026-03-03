from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('resume/', resume, name='resume'),
]
