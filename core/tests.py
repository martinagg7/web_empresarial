from django.test import TestCase
from django.urls import reverse




class CoreURLTests(TestCase):
    def test_home_url(self):
        url = reverse('home') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) #comprobar que devuelva la pag