from django.contrib import admin

from api.models import Rating, Product

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'rating'] 
    list_filter = ['product', 'user']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    search_fields = ['name', 'description']
    list_filter = ['name','description', 'price']

admin.site.register(Rating, RatingAdmin)
admin.site.register(Product, ProductAdmin)  
 