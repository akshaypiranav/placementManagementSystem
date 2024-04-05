from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Department,Student,Company,Drive,PassedOut,Application])