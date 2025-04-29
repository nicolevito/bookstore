import factory 

from django.contrib.auth.models import User
from product.models import ProductFactory

from order.models import Order

class UserFactory(factory.django.DjangoModelFactory):
    email = factory.faker('pystr')
    username = factory.Faker('pystr')
    
    class Meta:
        model = User
        
        
class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    
    @factory.post_generation
    def product(self, created, extrated, **kwargs):
        if not created: 
            return
        
        if extrated:
            for product in extrated:
                self.product.add(product)

    class Meta:
        model = Order