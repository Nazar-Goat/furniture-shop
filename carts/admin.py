from django.contrib import admin
from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model= Cart
    fields= 'product', 'quantity', 'created_timestamp'
    search_fields= 'product', 'quantity', 'created_timestamp'
    readonly_fields= ('created_timestamp', )
    extra= 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['display_user', 'display_product', 'quantity', 'created_timestamp']
    list_filter= ['created_timestamp', 'user', 'product__name']

    def display_user(self, obj):
        if obj.user:
            return str(obj.user)
        return "Аннонимный пользователь"
    
    def display_product(self, obj):
        return str(obj.product.name)
    
    # user_display and product_display alter name of columns in admin panel
    display_user.short_description = "Пользователь"
    display_product.short_description = "Товар"