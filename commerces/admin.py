from django.contrib import admin
from .models import Address, PromoCode, Order, OrderPromo, OrderItem, OrderItemOption

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'title','line1','city')

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code','active','valid_from','valid_to')

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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','restaurant','status','total','created_at')
    list_filter = ('status','created_at')
    inlines = [OrderItemInline, OrderPromoInline]
