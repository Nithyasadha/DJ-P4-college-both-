from django.contrib import admin
from django.urls import path 
from arts_department.views import*

urlpatterns=[
    path('admin/',admin.site.urls),
    path('BCOM/',BCOM,name='BCOM'),
    path('BCA/',BCA,name='BCA'),
]