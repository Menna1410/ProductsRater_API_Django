from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# uuid is a universally unique identifier that can be used as a primary key for database models. It is a 128-bit number that is typically represented as a string of hexadecimal digits. Using uuid as a primary key can help to ensure that each record in the database has a unique identifier, which can be useful for various applications, such as distributed systems or when merging data from multiple sources. In Django, you can use the UUIDField to define a field that will store a uuid value.    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'Rating {self.rating} for {self.product.name}'
    


    class Meta:
        unique_together = (('user', 'product'),) # This ensures that a user can only rate a product once
        indexes = [
            models.Index(fields=['user', 'product']),
        ]  # This creates an index on the user and product fields to improve query performance when filtering by these fields
