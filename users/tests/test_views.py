from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.models import User

user= get_user_model()

class UserLoginViewTest(TestCase):
    def setUp(self):
        self.password = "testpass123"
        self.user = User.objects.create_user(
            username="testuser", email="test@mail.com", password=self.password
        )

    def test_login_page_returns_200(self):
        url = reverse("user:login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_login_valid_user_redirects_home(self):
        url = reverse("user:login")
        response = self.client.post(url, {"username": "testuser", "password": self.password})
        self.assertRedirects(response, reverse("main:index"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_user_stays_on_page(self):
        url = reverse("user:login")
        response = self.client.post(url, {"username": "wrong", "password": "wrong"})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class UserRegistrationViewTest(TestCase):
    def test_register_new_user(self):
        url= reverse("users:registration")
        response= self.client.post(
            url,
            {
                "first_name": "John",
                "last_name": "Pork",
                "username": "NewUser",
                "email": "newuser@gmail.com",
                "password1": "Passnew123",
                "password2": "Passnew123"
            }
        )
        self.assertRedirects(response, reverse("user:profile"))
        self.assertTrue(User.objects.filter(username= "NewUser").exists())

class UserProfileViewTest(TestCase):
    def setUp(self):
        self.password = "testpass123"
        self.user = User.objects.create_user(
            username="testuser", email="test@mail.com", password=self.password
        )

    def test_profile_page_if_authenticated(self):
        self.client.login(username= "testuser", password= self.password)
        url= reverse("users:profile")
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")
        self.assertContains(response, "Home - Кабинет")

class UserCartViewTest(TestCase):
    def test_cart_page_returns_200(self):
        url= reverse("users:users_cart")
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/users_cart.html")

class LogoutViewTest(TestCase):
    def setUp(self):
        self.password = "testpass123"
        self.user = User.objects.create_user(
            username="testuser", email="test@mail.com", password=self.password
        )
    
    def test_logout_user(self):
        self.client.login(username= "testuser", password= self.password)
        url= reverse("users:logout")
        response= self.client.get(url)
        self.assertRedirects(response, reverse("main:index"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

        