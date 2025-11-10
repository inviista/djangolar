from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal
from abstracts.models import AbstractSoftDeletableModel

User = get_user_model()

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class AllObjectsManager(models.Manager):
    pass

class Address(AbstractSoftDeletableModel):
    objects = ActiveManager()
    all_objects = AllObjectsManager()
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=True)
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return f"{self.title} — {self.line1}"
        return f"{self.line1}, {self.city}"

class PromoCode(AbstractSoftDeletableModel):
    objects = ActiveManager()
    all_objects = AllObjectsManager()
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    percent = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
    fixed_amount = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
    active = models.BooleanField(default=True)
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    def is_valid(self):
        now = timezone.now()
        if not self.active:
            return False
        if self.valid_from and now < self.valid_from:
            return False
        if self.valid_to and now > self.valid_to:
            return False
        return True

    def __str__(self):
        return self.code

class Order(AbstractSoftDeletableModel):
    objects = ActiveManager()
    all_objects = AllObjectsManager()
    STATUS_NEW = 'new'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_DELIVERING = 'delivering'
    STATUS_DONE = 'done'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_DELIVERING, 'Delivering'),
        (STATUS_DONE, 'Done'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('catalogs.Restaurant', related_name='orders', on_delete=models.PROTECT)
    address = models.ForeignKey(Address, related_name='orders', on_delete=models.PROTECT)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=Decimal('0.00'))
    discount_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=Decimal('0.00'))
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=Decimal('0.00'))

    promos = models.ManyToManyField(PromoCode, through='OrderPromo', related_name='orders', blank=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.user}"

class OrderPromo(AbstractSoftDeletableModel):
    objects = ActiveManager()
    all_objects = AllObjectsManager()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    promo = models.ForeignKey(PromoCode, on_delete=models.PROTECT)
    applied_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order', 'promo'], name='unique_order_promo')
        ]

    def __str__(self):
        return f"{self.promo.code} on Order {self.order_id}: -{self.applied_amount}"

class OrderItem(AbstractSoftDeletableModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item_id = models.PositiveIntegerField()
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])  # unit price at order time
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    line_total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])  # item_price * quantity + options

    def __str__(self):
        return f"{self.item_name} x{self.quantity} (Order {self.order_id})"

class OrderItemOption(AbstractSoftDeletableModel):
    order_item = models.ForeignKey(OrderItem, related_name='options', on_delete=models.CASCADE)
    option_id = models.PositiveIntegerField(null=True, blank=True)
    option_name = models.CharField(max_length=255)
    price_delta = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.option_name} (+{self.price_delta})"
