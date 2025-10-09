
from django.test import TestCase

from goods.models import Categories, Products


class ProductModelTest(TestCase):
    def setUp(self):
        self.category= Categories.objects.create(name="Интерьер", slug='Interior')
        self.product= Products.objects.create(
            name= 'Полка',
            slug= 'Polka',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )

    def test_str_returns_name_and_quantity(self):
        expected= "Полка . Количество- 5"
        self.assertEqual(str(self.product), expected)
        
    def test_sell_price_with_discount(self):
        self.assertEqual(self.product.sell_price(), 900.00)

    def test_sell_price_without_discount(self):
        self.product.discount= None
        self.assertEqual(self.product.sell_price(), 1000.00)

    def test_get_id(self):
        self.assertEqual(len(self.product.get_id()), 5)
        self.assertTrue(self.product.get_id().isdigit())
        