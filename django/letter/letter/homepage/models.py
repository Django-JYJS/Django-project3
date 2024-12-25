from django.db import models

# Create your models here.

from django.urls import reverse

class mail(models.Model):
    detail = models.TextField(max_length=10000, help_text="내용을 입력해주세요")

    def __str__(self):
        return self.detail[:50]  # 내용의 처음 50자를 반환 (어드민에서 보여질 내용)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    


import uuid
    

