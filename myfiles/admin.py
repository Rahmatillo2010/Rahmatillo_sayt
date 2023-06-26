from django.contrib import admin
from myfiles.models import *

# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'description', 'deadline', 'type', 'company_name', 'pictures1']
admin.site.register(Portfolio,AdminPortfolio)



class AdminType(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Type,AdminType)


class AdminServis(admin.ModelAdmin):
    list_display = ['id', 'pictures1', 'name', 'description']


admin.site.register(Services,AdminServis)



class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'pictures1', 'name', 'lavozim', 'description']


admin.site.register(Team,AdminTeam)


class AdminMalumot(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'subject', 'message']

admin.site.register(Malumot_saqlash,AdminMalumot)

class AdminSubr(admin.ModelAdmin):
    list_display = ['id', 'email', 'date']

admin.site.register(Subr,AdminSubr)

