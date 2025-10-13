from django.contrib import admin
from .models import Address, PromoCode, Order, OrderPromo, OrderItem, OrderItemOption

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'line1', 'city', 'is_deleted')
    list_filter = ('city', 'is_deleted')
    actions = ["restore_items"]

    def get_queryset(self, request):
        return self.model.all_objects.all()

    @admin.action(description="Восстановить")
    def restore_items(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'active', 'valid_from', 'valid_to', 'is_deleted')
    list_filter = ('active', 'is_deleted')
    actions = ["restore_items"]

    @admin.action(description="Восстановить")
    def restore_items(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)

    def get_queryset(self, request):
        return self.model.all_objects.all()

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'status', 'total', 'is_deleted', 'created_at')
    list_filter = ('status', 'is_deleted', 'created_at')
    actions = ["restore_items"]

    def get_queryset(self, request):
        return self.model.all_objects.all()

    @admin.action(description="Восстановить")
    def restore_items(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)

class OrderPromoInline(admin.TabularInline):
    model = OrderPromo
    extra = 0
    readonly_fields = ('applied_amount',)

class OrderItemOptionInline(admin.TabularInline):
    model = OrderItemOption
    extra = 0

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0
    inlines = [OrderItemOptionInline]

