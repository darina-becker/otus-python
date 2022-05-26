from lib2to3.pytree import Node
from urllib import response
from app.models import App, AppKind, AppAgeLimit
from django.test import TestCase


# Create your tests here.

class AppTest(TestCase):
    
    def setUp(self):

        self.kind_prep = {'name': 'finance'}
        AppKind.objects.get_or_create(name=self.kind_prep['name'])

        self.age = {'name':'G', 'desc':'General Audience', 'age': 3}
        AppAgeLimit.objects.get_or_create(name=self.age['name'], description=self.age['desc'], min_age=self.age['age'])
        
        self.test_data = {
            'name': 'Tinkoff',
            'desc': 'The best online bank in the world',
            'kind': 1,
            'age_limit': 1,
            'download_counter': 1000,
        }

        self.expected_data = {
            'name': 'Tinkoff',
            'desc': 'The best online bank in the world',
            'kind': 'finance',
            'age_limit': 'G',
            'download_counter': 1000,
        }

    def tearDown(self):

        AppKind.objects.filter(name=self.kind_prep['name']).delete()
        AppAgeLimit.objects.filter(name=self.age['name']).delete()

        self.kind_prep = None
        self.age = None
        self.test_data = None
        self.expected_data = None
    
    def test_create(self):

        response = self.client.post('/app/create/', data=self.test_data)
        self.assertEqual(302, response.status_code)

        new_app = App.objects.get(name=self.test_data['name'])

        self.assertEqual(new_app.name, self.expected_data['name'])
        self.assertEqual(new_app.desc, self.expected_data['desc'])
        self.assertEqual(new_app.kind.name, self.expected_data['kind'])
        self.assertEqual(new_app.age_limit.name, self.expected_data['age_limit'])
        self.assertEqual(new_app.download_counter, self.expected_data['download_counter'])

    def test_context(self):

        response = self.client.post('/app/create/', data=self.test_data)
        self.assertEqual(302, response.status_code)
        
        response = self.client.get('/app/detail/1/')
        self.assertEqual(response.context['app'].name, self.test_data['name'])
