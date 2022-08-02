
from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('resume/', resume, name='resume'),
    path('services/', services, name='services'),
    path('service-details/<id>', service_details, name='service_details'),
    path('project/', project, name='project'),
    path('project-details/<id>', project_details, name='project_details'),
    #path('portfolio/', portfolio, name='portfolio'),
    #path('portfolio-details/<id>', portfolio_details, name='portfolio_details'),
    path('contact/', contact, name='contact'),
    
]