from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snack

class SnackModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='ali2',password='123456')
        test_user.save()

        test_snack = Snack.objects.create(
            purchaser = test_user,
            title = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_snack.save()

    def test_blog_content(self):
        snack = Snack.objects.get(id=1)

        self.assertEqual(str(snack.purchaser), 'ali2')
        self.assertEqual(snack.title, 'Title of Blog')
        self.assertEqual(snack.description, 'Words about the blog')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('snacks_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='ali2',password='123456')
        test_user.save()

        test_snack = Snack.objects.create(
            purchaser = test_user,
            title = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_snack.save()

        response = self.client.get(reverse('snack_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'title': test_snack.title,
            'description': test_snack.description,
            'purchaser': test_user.id,
        })