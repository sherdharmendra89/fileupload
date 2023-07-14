from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import File, CustomUser

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superuser = CustomUser.objects.create_superuser(username='admin', password='admin123')
        self.client.force_authenticate(user=self.superuser)

    # def test_file_upload_api(self):
    #     url = reverse('file-upload')
    #     with open('files/f.txt' , 'rb') as file:
    #         response = self.client.post(url, {'file': file}, format='multipart')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_file_list_api(self):
        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_file_download_api(self):
    #     file = File.objects.create(file='files/f.txt')
    #     url = reverse('file-download', args=[file.pk])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_create_view(self):
        url = reverse('superuser-create')
        data = {
            'username': 'testadmin',
            'password': 'testadmin123',
            'is_staff': True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
