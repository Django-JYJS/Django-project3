from django.db import models

# Create your models here.

from django.urls import reverse

class mail(models.Model):
    title = models.CharField(max_length=200) #제목
    name = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    detail = models.TextField(max_length=10000,help_text="내용을 입력해주세요")

    def __str__(self) :
        return self.title
    

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    

import uuid
    

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name =  models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name','first_name']


    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])
    def __str__(self):
        return f'{self.last_name},{self.first_name}'

