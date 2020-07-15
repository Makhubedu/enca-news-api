from django.contrib import admin
from .models import News, MainNews,ReadNews


# Register your models here.
admin.site.register(News)
admin.site.register(MainNews)
admin.site.register(ReadNews)