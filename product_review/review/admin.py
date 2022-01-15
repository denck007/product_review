from django.contrib import admin

from .models import Brand, Product, Review, Store, Tag

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Store)
admin.site.register(Tag)
