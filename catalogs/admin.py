from django.contrib import admin
from .models import Restaurant, Category, Option, MenuItem, ItemCategory, ItemOption

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'default_price_delta')

class ItemCategoryInline(admin.TabularInline):
    model = ItemCategory
    extra = 1

class ItemOptionInline(admin.TabularInline):
    model = ItemOption
    extra = 1

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name','restaurant','base_price','is_active','created_at')
    list_filter = ('restaurant', 'is_active')
    inlines = [ItemCategoryInline, ItemOptionInline]
