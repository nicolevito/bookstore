import factory

from product.models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Iterator([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    price = factory.Faker('pyint')

    @factory.post_generation
    def category(self, create, extracted, **kwargs):  
        if extracted:
            self.category.set(extracted)

        if extracted:
            for cat in extracted:
                self.category.add(cat) 

    class Meta:
        model = Product
