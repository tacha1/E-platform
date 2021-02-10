from django.contrib import admin
from .models import service,Profile,Comments,Rating

# Register your models here.
admin.site.register(service)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Rating)