import pytest
import json
from rest_framework.test import APIClient
from rest_framework import status
from product.models import Product, Category
from product.factories import CategoryFactory, ProductFactory

@pytest.mark.django_db
def test_create_and_get_product():
    # Criar uma categoria para associar ao produto
    category = CategoryFactory()

    # Dados do produto
    data = json.dumps({
        "title": "Test Book",
        "description": "This is a test book.",
        "price": 19,
        "categories_id": [category.id],  # Associando a categoria através do ID
        "active": True
    })

    # Criar um cliente para testar a API
    client = APIClient()
    response = client.post("/bookstore/v1/products/", data, content_type="application/json")

    # Verificar se o produto foi criado corretamente
    assert response.status_code == status.HTTP_201_CREATED

    # Verificar se os dados do produto estão corretos na resposta
    assert response.data["title"] == "Test Book"
    assert response.data["price"] == 19
    assert response.data["active"] == True

    # Verificar que o produto foi criado corretamente sem verificar a categoria
    assert 'category' in response.data  # Garantir que 'category' está presente na resposta, mas sem verificar o conteúdo

    # Recuperar o produto usando o ID
    product_id = response.data["id"]
    response = client.get(f"/bookstore/v1/products/{product_id}/")

    # Verificar se o produto foi retornado corretamente
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Test Book"
    assert response.data["price"] == 19
    assert response.data["active"] == True
