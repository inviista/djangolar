from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def __str__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    default_price_delta = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(Category, through='ItemCategory', related_name='items')
    options = models.ManyToManyField(Option, through='ItemOption', related_name='items')

    def __str__(self):
        return f"{self.name} — {self.restaurant.name}"

class ItemCategory(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)  # order inside category

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['menu_item', 'category'], name='unique_item_category_pair')
        ]
        ordering = ['position']

    def __str__(self):
        return f"{self.menu_item} in {self.category} ({self.position})"

class ItemOption(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    price_delta = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])
    is_default = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['menu_item', 'option'], name='unique_item_option_pair')
        ]

    def __str__(self):
        return f"{self.option} for {self.menu_item} (+{self.price_delta})"
