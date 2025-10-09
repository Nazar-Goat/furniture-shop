from django.test import TestCase
from django.urls import reverse

from goods.models import Categories, Products


class CatalogViewTest(TestCase):
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

        self.product= Products.objects.create(
            name= 'Шкаф',
            slug= 'Sckaf',
            price= 1000,
            discount= 10,
            quantity= 5,
            category= self.category
        )
    def test_catalog_returns_200(self):
        url= reverse("catalog:index", kwargs={"category_slug": "Interior"})
        responce= self.client.get(url)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, "Полка")
        self.assertContains(responce, "Шкаф")

    def test_catalog_all_returns_200(self):
        url= reverse("catalog:index", kwargs={"category_slug": "all"})
        responce= self.client.get(url)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, "Полка")
        self.assertContains(responce, "Шкаф")

    def test_catalog_returns_404(self):
        url= reverse("catalog:index", kwargs={"category_slug": "Unknown"})
        responce= self.client.get(url)
        self.assertEqual(responce.status_code, 404)

class ProductViewTests(TestCase):
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

    def test_catalog_returns_200(self):
        url= reverse("catalog:index", kwargs={"category_slug": "Interior"})
        responce= self.client.get(url)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, "Полка")

    def test_catalog_returns_404(self):
        url= reverse("catalog:index", kwargs={"category_slug": "Unknown"})
        responce= self.client.get(url)
        self.assertEqual(responce.status_code, 404)
