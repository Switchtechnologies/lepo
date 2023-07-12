from django.contrib import admin
from .models import perfume
# Register your models here.

class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name','img','desc','price','offer')
admin.site.register(perfume, PerfumeAdmin)