from django.urls import path, include
from rest_framework import routers
from escola.views import AlunosViewSet, TodosAlunosViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'todos/alunos', TodosAlunosViewSet, basename='Alunos')

alunos_urls = router.urls