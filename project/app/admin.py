from django.contrib import admin

# Register your models here.
from .models import Mobile,Company

admin.site.register(Mobile)
admin.site.register(Company)
