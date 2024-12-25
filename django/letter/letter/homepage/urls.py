from django.urls import path
from django.contrib import admin
from homepage import views
from . import views
urlpatterns =[  
    path('homepage/', views.homepage_view, name='homepage'),
    path('letter/', views.letter_view, name='letter_view'),
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('letter/finish/', views.finish_view, name ='finish'),
]
