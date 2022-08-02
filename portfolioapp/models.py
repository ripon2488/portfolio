from django.db import models
from django.contrib.auth.models import*
# Create your models here.


class About(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    short_desc=models.TextField(blank=True, null=True)
    desc=models.TextField(blank=True, null=True)
    expertised_designation=models.CharField(max_length=150,blank=True,null=True)
    designation_summery=models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    birthday=models.DateField(blank=True, null=True)
    website=models.CharField(max_length=50, blank=True, null=True)
    phone=models.CharField(max_length=12, blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    degree=models.CharField(max_length=50,blank=True,null=True)
    email=models.CharField(max_length=50,blank=True,null=True)
    freelunch=models.CharField(max_length=100,blank=True,null=True)
    skill_desc=models.TextField(blank=True, null=True)
    fact_desc=models.TextField(blank=True, null=True)
    testimonial_desc=models.TextField(blank=True, null=True)
    resume_desc=models.TextField(blank=True, null=True)
    resume_summery=models.TextField(blank=True, null=True)
    service_summery=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Skill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    skill_level=models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class Facts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    facts_nos=models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

class Testimonial(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    buyer_name=models.CharField(max_length=50,blank=True, null=True)
    buyer_designation=models.CharField(max_length=50, blank=True, null=True)
    testimonial_details=models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Education(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    education_title=models.CharField(max_length=100,blank=True, null=True)
    date_from=models.DateField()
    date_to=models.DateField(blank=True, null=True)
    institute_name=models.CharField(max_length=100,blank=True,null=True)
    education_desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


class ProfessionalExperience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=100,blank=True, null=True)
    date_from=models.DateField()
    date_to=models.DateField(blank=True, null=True)
    company_name=models.CharField(max_length=100,blank=True,null=True)
    responsibility=models.TextField(blank=True, null=True)
   
    def __str__(self):
        return str(self.job_title)

class Service(models.Model):
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    service_name=models.CharField(max_length=100, blank=True, null=True)
    service_desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.service_name)


class Project(models.Model):
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    project_img=models.ImageField (blank=True, null=True)
    project_title=models.CharField(max_length=100, blank=True, null=True)
    project_desc=models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.project_title)