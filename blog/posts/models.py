from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def short_description(self, word_limit=30):
        """
        Return a truncated description of the product.
        If the description has more words than `word_limit`, truncate it and add an ellipsis.
        """
        words = self.description.split()
        if len(words) > word_limit:
            return ' '.join(words[:word_limit]) + '...'
        return self.description

    def clean(self):
        """
        Override this method to add any custom validation logic.
        """
        super().clean()

# It's better to handle product editing logic in a form or service layer

def update_product(product, name, description, image):
    """
    Update the product instance with the given fields.
    """
    product.name = name
    product.description = description
    product.image = image
    product.save()
    return product

