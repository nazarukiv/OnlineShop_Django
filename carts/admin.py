from django.contrib import admin
from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ("created_timestamp", )
    extra = 1



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['product_display','product_display', 'user', 'product', 'quantity', 'created_timestamp']
    list_filter = ['user', 'product', 'created_timestamp']

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Anonym user"


    def product_display(self, obj):
        return str(obj.product_name)