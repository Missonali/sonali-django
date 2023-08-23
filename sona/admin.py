from django.contrib import admin
from .models import contact2

# Register your models here.

class adminmodels(admin.ModelAdmin):
    list_display=['name','email','number','message']
    
admin.site.register(contact2,adminmodels)
    