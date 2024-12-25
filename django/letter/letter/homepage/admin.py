from django.contrib import admin

# Register your models here.
from homepage.models import Mail

class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'detail')

admin.site.register(Mail,MailAdmin)
