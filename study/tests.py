from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from config import settings
from study.models import Study, Materials
from users.models import User


class MaterialsTestCase(APITestCase):

    def setUp(self):
        """Заполнение данных"""

        self.user = User.objects.create(
            email='testing_user@adm.com',
            is_staff=True,
            is_superuser=True,
            is_active=True,

        )
        self.user.set_password('324214Kross!')
        self.user.save()

        token = RefreshToken.for_user(self.user)
        self.access_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.study = Study.objects.create(
            title='Django_drf guide',
        )

        self.materials = Materials.objects.create(
            title='video lesson',
            content='video content',
            study_materials=self.study,
            autor='Unknown'
        )

    def test_materials_list(self):
        """ Тест получения списка материалов для обучения"""

        response = self.client.get(
            reverse('study:materials_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.materials.id,
                        "title": self.materials.title,
                        "content": self.materials.content,
                        "study_materials": self.materials.study_materials.title,
                        "autor": self.materials.autor
                    }
                ]
            }
        )

    def test_materials_create(self):
        """Тест создания материала"""

        response = self.client.post('/materials/create/',
                                    {'title': 'video lesson', 'content': 'video content',
                                     'study_materials': self.materials.study_materials.title, 'autor': 'Unknown'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_materials_update(self):
        """ Тест обновления материала """
        self.client.force_authenticate(user=self.user)

        response = self.client.patch(reverse('study:materials_update', args=[self.materials.pk]),
                                     {'title': 'video lesson', 'content': 'video content',
                                      'study_materials': self.materials.study_materials.title, 'autor': 'Unknown'})

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        self.assertTrue(
            Materials.objects.all().exists()
        )

    def test_materials_delete(self):
        """ Тест удаления материала """

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse('study:materials_delete', args=[self.materials.pk]))

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Materials.objects.all().exists(),
        )

    def tearDown(self) -> None:
        self.user.delete()
        self.study.delete()
        self.materials.delete()