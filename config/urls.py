from django.contrib import admin
from django.urls import path, include
from escola.urls import alunos_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(alunos_urls))
]
