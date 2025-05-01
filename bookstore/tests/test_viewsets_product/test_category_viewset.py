from product.factories import CategoryFactory, ProductFactory
from product.models import Product, Category
from rest_framework.test import APITestCase
from django.urls import reverse
import json
from rest_framework import status


class TestCategoryViewSet(APITestCase):
    
    def setUp(self):
        self.category = CategoryFactory(title='books')
        
        
    def test_get_all_category(self):
        response = self.client.get(
            reverse('category-list', kwargs={'version': 'v1'})
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)
        
        self.assertEqual(category_data[0]['title'], self.category.title)
        
    def test_create_category(self):
        data = json.dumps({
            'title': 'technology',
            'slug': 'technology-slug',
       })
        
        response = self.client.post(
            reverse('category-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        
        print(response.data) 
                
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        created_category = Category.objects.get(title='technology')
        
        self.assertEqual(created_category.title, 'technology')

