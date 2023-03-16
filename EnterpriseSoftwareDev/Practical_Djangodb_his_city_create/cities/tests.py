from .models import City
from django.test import TestCase, Client

# Create your tests here.

class CityViewTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        City.objects.create(
            city = 'Uruk',
            otherName = 'Eech',
            country = 'Iraq',
            latitude = 31.3222,
            longitude = 45.6609,
            year = 3500,
            pop = 14000,
            city_id = 'uruk.31.3_45, 6'
        )

        City.objects.create(
            city = 'Uruk',
            otherName = 'E4ech',
            country = 'Iraq',
            latitude = 31.3222,
            longitude = 45.6609,
            year = 3500,
            pop = 14000,
            city_id = 'uruk.31.3_45, 6'
        )

        return super().setUpTestData()

    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Historic')

    def test_cities(self):
        client = Client()
        response = self.client.get('/cities/Uruk')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is Uruk')

    def test_city_list(self):
        cities = City.cities()
        self.assertEqual(cities.count(), 2)