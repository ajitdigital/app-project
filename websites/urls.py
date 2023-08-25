from django.urls import path
from  websites.views import index, about, service, gallery, faq, contact 

app_name = 'websites'

urlpatterns = [
    path('', index, name='index.html'),
    path('about/', about, name='about.html'),
    path('service/', service, name='service.html'),
    path('gallery/', gallery, name='gallery.html'),
    path('faq/', faq, name='faq.html'),
    path('contact/', contact, name='contact.html'),

]




