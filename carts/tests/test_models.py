from django.contrib.auth import get_user_model
from django.test import TestCase

from carts.models import Cart
from goods.models import Categories, Products

User= get_user_model()
class CartModelsTest(TestCase):
    def setUp(self):
        self.user= User.objects.create(username= "testuser", password= "12345")
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )

        self.cart= Cart.objects.create(user= self.user, product= self.product, quantity= 2)

    def test_products_price(self):
        expected_price= round(self.product.sell_price() * self.cart.quantity, 2)
        self.assertEqual(self.cart.products_price(), expected_price)

    def test_str(self):
        self.assertIn(self.user.username, str(self.cart))
        self.assertIn(self.product.name, str(self.cart))
        self.assertIn(str(self.cart.quantity), str(self.cart))

