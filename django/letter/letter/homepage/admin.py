from django.contrib import admin

# Register your models here.
from homepage.models import Author, mail


admin.site.register(Author)
admin.site.register(mail)
