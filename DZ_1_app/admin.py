from django.contrib import admin
from DZ_1_app.models import Category, Product, Review


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)