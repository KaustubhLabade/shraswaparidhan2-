from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    # 👇 This creates subcategory feature
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    def __str__(self):
        return self.name

class Dress(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dresses')
    size = models.CharField(max_length=20)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='dresses/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name