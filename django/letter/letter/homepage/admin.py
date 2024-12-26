# from django.contrib import admin

# # Register your models here.
# from homepage.models import Mail

# class MailAdmin(admin.ModelAdmin):
#     list_display = ('id', 'detail')

# admin.site.register(Mail,MailAdmin)

from django.contrib import admin
from .models import Mail

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('detail',)  # 어드민 페이지에서 보이는 필드
