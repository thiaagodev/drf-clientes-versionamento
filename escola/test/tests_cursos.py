from rest_framework.test import APITestCase
from django.urls import reverse

from escola.models import Curso


class CursosTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao = 'Curso de Teste 1', nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso = 'CTT2', descricao = 'Curso de Teste 2', nivel = 'A'
        )

    def test_falhador(self):
        self.fail('Teste Falhou de proprósito!')