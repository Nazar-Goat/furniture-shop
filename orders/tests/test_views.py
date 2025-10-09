from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from carts.models import Cart
from goods.models import Categories, Products
from orders.models import Order, OrderItem


User= get_user_model()

class CreateOrderViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )
        self.client.force_login(self.user)

        # Добавляем товар в корзину
        Cart.objects.create(user=self.user, product=self.product, quantity=2)

    def test_order_valid(self):
        response = self.client.post(reverse('orders:create_order'), {
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '1234567890',
            'requires_delivery': 1,
            'delivery_address': 'Test Street 1',
            'payment_on_get': 1,
        })

        # Проверяем редирект после успешного оформления
        self.assertEqual(response.status_code, 302)

        # Проверяем, что заказ создался
        self.assertTrue(Order.objects.filter(user=self.user).exists())

        order = Order.objects.get(user=self.user)
        self.assertEqual(order.orderitem_set.count(), 1)
        self.assertEqual(order.orderitem_set.first().product, self.product)