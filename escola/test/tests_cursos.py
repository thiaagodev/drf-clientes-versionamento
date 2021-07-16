from rest_framework.test import APITestCase
from rest_framework import status
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

    # def test_falhador(self):
    #     self.fail('Teste Falhou de proprósito!')

    def test_requisicao_get_para_listar_todos_os_cursos(self):
        """ Teste para verificar se a requisição GET para listar os cursos """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_um_curso(self):
        """ Teste para verificar se a requisição POST para criar um curso """
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso de Teste 3',
            'nivel': 'A'
        }

        response = self.client.post(self.list_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        """ Teste para verificar a requisição DELETE não permitida para deletar um curso """
        response = self.client.delete('/cursos/1/')
        
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """ Teste para verificar a requisição PUT para atualizar um curso """
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso de Teste 1 atualizado',
            'nivel': 'I'
        }

        response = self.client.put('/cursos/1/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
