# tests/test_myapp.py
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.contrib.auth import authenticate, login, logout

@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_register_view(client):
    response = client.post('/users/register/', {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
  

@pytest.mark.django_db
def test_login_view(client):
    User.objects.create_user(username='testuser', password='testpassword')
    response = client.post('/users/login/', {'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 302
    user = authenticate(username='testuser', password='testpassword')
    assert user is not None

@pytest.mark.django_db
def test_logout_view(client):
    User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get('/users/logout/')
    assert response.status_code == 302
    assert not client.session.get('_auth_user_id') 
