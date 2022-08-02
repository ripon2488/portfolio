from django.contrib import admin
from .models import*
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    list_display=('user','short_desc','desc')

class SkillAdmin(admin.ModelAdmin):
    list_display=('name','skill_level')

class FactsAdmin(admin.ModelAdmin):
    list_display=('name','facts_nos')

class TestimonialAdmin(admin.ModelAdmin):
    list_display=('user','buyer_name','buyer_designation','testimonial_details')

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','birthday','website','phone','city')

class EducationAdmin(admin.ModelAdmin):
    list_display=('user','education_title','date_from','date_to','institute_name','education_desc')

class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display=('user','job_title','date_from','date_to','company_name','responsibility')
class ServiceAdmin(admin.ModelAdmin):
    list_display=('user','service_name','service_desc')
class ProjectAdmin(admin.ModelAdmin):
    list_display=('user','project_title','project_desc')

admin.site.register(About,AboutAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Facts,FactsAdmin)
admin.site.register(Testimonial,TestimonialAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(ProfessionalExperience,ProfessionalExperienceAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Project,ProjectAdmin)