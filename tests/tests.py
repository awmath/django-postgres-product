from decimal import Decimal

from django.test import TestCase

from postgres_product.aggregates import Product
from tests.models import TestModel


class ProductAggregationTest(TestCase):
    def setUpTestData():
        instances = [TestModel(int_field=int(n), float_field=float(n), decimal_field=Decimal(n)) for n in [x + 1 for x in range(4)]]
        TestModel.objects.bulk_create(instances)

    def test_aggregate(self):
        self.assertEqual(TestModel.objects.all().aggregate(product=Product('int_field'))['product'], 24)
        self.assertEqual(TestModel.objects.all().aggregate(product=Product('decimal_field'))['product'], 24)
        self.assertEqual(TestModel.objects.all().aggregate(product=Product('float_field'))['product'], 24)
