from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Cultivo, Variedad, Produccion
from datetime import date

class CultivosAPITest(APITestCase):
    def setUp(self):
        self.cult = Cultivo.objects.create(nombre='Maíz')
        self.var = Variedad.objects.create(cultivo=self.cult, nombre='VarA')
        self.prod = Produccion.objects.create(
            variedad=self.var,
            ciclo='C-2025',
            fecha_inicio=date(2025,1,1),
            fecha_fin=date(2025,6,1),
            cantidad_planeada=1000,
            unidad='kg'
        )

    def test_create_cultivo(self):
        resp = self.client.post('/api/cultivos/', {'nombre': 'Trigo', 'descripcion': 'Trigo común'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_list_variedades_filter_by_cultivo(self):
        resp = self.client.get('/api/variedades/', {'cultivo': self.cult.id})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertTrue(len(data) >= 1)
        self.assertEqual(data[0]['cultivo'], self.cult.id)

    def test_produccion_filters_and_detail(self):
        # listar
        resp = self.client.get('/api/producciones/', {'ciclo': 'C-2025'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # detalle
        pid = self.prod.id
        resp2 = self.client.get(f'/api/producciones/{pid}/')
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)

    def test_resumen_por_cultivo(self):
        resp = self.client.get('/api/producciones/resumen_por_cultivo/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertTrue(isinstance(data, list))
        # debe incluir el cultivo creado
        ids = [d['cultivo_id'] for d in data]
        self.assertIn(self.cult.id, ids)
