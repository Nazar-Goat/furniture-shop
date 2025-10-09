from itertools import product
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from carts.models import Cart
from goods.models import Categories, Products
from users.models import User

User= get_user_model()

class CartAddViewTest(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username= "testuser", password= "12345")
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )

        self.client.login(username="testuser", password="12345")
    def test_cart_add_returns_200(self):
        url= reverse("cart:cart_add")
        
        response= self.client.post(url, {"product_id": self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Cart.objects.filter(user=self.user, product=self.product).exists())


class CartChangeViewTest(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username= "testuser", password= "12345")
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )

        self.client.login(username="testuser", password="12345")

    def test_cart_change_responce_200(self):
        cart= Cart.objects.create(user=self.user, product=self.product, quantity=1)
        url= reverse("cart:cart_change")

        response= self.client.post(url, {"cart_id": cart.id, "quantity": 2})

        self.assertEqual(response.status_code, 200)
        cart_item= Cart.objects.get(user=self.user, product=self.product)
        self.assertEqual(cart_item.quantity, 2)


class CartRemoveViewTest(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username= "testuser", password= "12345")
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )

        self.client.login(username="testuser", password="12345")

    def test_cart_remove(self):
        cart= Cart.objects.create(user=self.user, product=self.product, quantity=2)
        url= reverse("cart:cart_remove")

        response= self.client.post(url, {"cart_id": cart.id})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(id=cart.id).exists())

