from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
          name="BURHAN SHOES",
          price=3000000,
          description="Sepatu bola edisi BURHAN FC",
          category="shoes",
          is_featured=True
        )
        self.assertTrue(product.price, 3000000)
        self.assertEqual(product.name, "BURHAN SHOES")
        self.assertTrue(product.is_featured)
        
    def test_product_default_values(self):
        product = Product.objects.create(
          name="Jersey BURHAN FC x Adidas",
          price=150000,
          description="Jersey BURHAN x PUMA 2025",category="apparel",
        )
        self.assertIsNone(product.thumbnail)
        self.assertFalse(product.is_featured)
        
        
    def test_product_category_choice(self):
        product = Product.objects.create(
            name="Handglove Keeper",
            price=100000,
            description="Limited edition handglove",
            category="goalkeeper geer",
        )
        self.assertEqual(product.category, "goalkeeper geer")


