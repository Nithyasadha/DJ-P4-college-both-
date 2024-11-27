from django.contrib import admin
from django.urls import path 
from medical_department.views import*

urlpatterns=[
    path('admin/',admin.site.urls),
    path('MBBS/',MBBS,name='MBBS'),
    path('MPHARM/',MPHARM,name='MPHARM'),
]