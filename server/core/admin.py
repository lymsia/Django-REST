from django.contrib import admin
from core.models import Purchaser, Product, History

# Register your models here.
admin.site.register(Purchaser)
admin.site.register(Product)
admin.site.register(History)

