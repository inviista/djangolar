from django.contrib import admin
from .models import Restaurant, Category, Option, MenuItem, ItemCategory, ItemOption

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "is_deleted", "deleted_at")
    list_filter = ("is_deleted",)
    search_fields = ("name",)
    actions = ["restore_items"]

    def get_queryset(self, request):
        return Restaurant.all_objects.all()

    @admin.action(description="Восстановить выбранные рестораны")
    def restore_items(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)

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
    list_display = ('name', 'restaurant', 'base_price', 'is_active', 'is_deleted', 'deleted_at', 'created_at')
    list_filter = ('restaurant', 'is_active', 'is_deleted')
    search_fields = ('name',)
    inlines = [ItemCategoryInline, ItemOptionInline]
    actions = ["restore_items"]

    def get_queryset(self, request):
        return MenuItem.all_objects.all()

    @admin.action(description="Восстановить выбранные блюда")
    def restore_items(self, request, queryset):
        queryset.update(is_deleted=False, deleted_at=None)
