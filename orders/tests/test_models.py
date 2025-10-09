from django.contrib.auth import get_user_model
from django.test import TestCase

from goods.models import Categories, Products
from orders.models import Order, OrderItem
from users.models import User

User= get_user_model()
class OrderModelTests(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(
            username= "username",
            password= "12345"
        )

        self.order = Order.objects.create(
            user=self.user,
            phone_number="1234567890",
            requires_delivery=True,
            delivery_address="Test street 1",
            payment_on_get=True,
        )

    def test_str(self):
        self.assertIn(str(self.order.pk), str(self.order))
        self.assertIn(self.user.first_name, str(self.order))

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(
            username= "username",
            password= "12345"
        )
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )

        self.order = Order.objects.create(
            user=self.user,
            phone_number="1234567890",
        )

        self.order_item= OrderItem.objects.create(
            order= self.order,
            product= self.product,
            name=  self.product.name,
            price= self.product.sell_price(),
            quantity= 2
        )

    def test_str(self):
        self.assertIn(str(self.order.pk), str(self.order_item))
        self.assertIn(self.product.name, str(self.order_item))

    def test_products_price(self):
        expected_price= round(self.product.sell_price() * self.order_item.quantity, 2)
        self.assertEqual(self.order_item.products_price(), expected_price)

