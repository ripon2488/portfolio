from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import*
# Create your views here.
from .models import*

def index(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user) 
    profile=Profile.objects.get(user=user) 
    context={'user_info':user_info,'profile':profile}
    return render(request,'index.html',context)

def about(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user) 
    about_user=About.objects.get(user=user)
    skills=Skill.objects.filter(user=user).order_by('skill_level').reverse()
    facts=Facts.objects.filter(user=user) 
    testimonials=Testimonial.objects.filter(user=user)
    profile=Profile.objects.get(user=user) 
    context={'about_user':about_user,'profile':profile,'user_info':user_info,'skills':skills,
            'facts':facts,'testimonials':testimonials}
    return render(request,'about.html',context)

def resume(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    about_user=About.objects.get(user=user)
    educations=Education.objects.filter(user=user)
    my_experiance=ProfessionalExperience.objects.filter(user=user)
    context={'user_info':user_info,'profile':profile,'about_user':about_user,'educations':educations,
            'my_experiance':my_experiance}
    return render(request,'resume.html',context)

def services(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    about_user=About.objects.get(user=user)
    my_service=Service.objects.filter(user=user)
    context={'user_info':user_info,'profile':profile,'about_user':about_user,'my_service':my_service}
    return render(request,'services.html',context)

def service_details(request,id):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    about_user=About.objects.get(user=user)
    services=Service.objects.get(id = id)
    print(services.service_desc)
    context={'user_info':user_info,'profile':profile,'about_user':about_user,'services':services}
    return render(request,'service-details.html',context)

def portfolio(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    context={'user_info':user_info,'profile':profile}
    return render(request,'portfolio.html',context)

def portfolio_details(request,id):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    portfolio_desc=Profile.objects.get(id=id) 
    context={'user_info':user_info,'profile':profile,'portfolio_desc':portfolio_desc}
    return render(request,'portfolio-details.html',context)
def project(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    about_user=About.objects.get(user=user)
    user_project=Project.objects.filter(user=user)
    my_service=Service.objects.filter(user=user)
    context={'user_info':user_info,'profile':profile,'about_user':about_user,'my_service':my_service,
    'user_project':user_project}
    return render(request,'project.html',context)

def project_details(request,id):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    about_user=About.objects.get(user=user)
    user_project=Project.objects.filter(user=user)
    services=Service.objects.get(id = id)
    print(services.service_desc)
    context={'user_info':user_info,'profile':profile,'about_user':about_user,'services':services,
    'user_project':user_project}
    return render(request,'project-details.html',context)

def contact(request):
    user='ripon'
    user=User.objects.get(username=user)
    user_info=User.objects.get(username=user)
    profile=Profile.objects.get(user=user) 
    context={'user_info':user_info,'profile':profile}
    return render(request,'contact.html',context)    