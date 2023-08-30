from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Check if registration redirects
        self.assertTrue(User.objects.filter(username='testuser').exists())


    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)  # Check if login is successful
        self.assertTrue(User.objects.filter(username='testuser').exists())

    
      
