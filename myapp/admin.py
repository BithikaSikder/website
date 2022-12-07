from django.contrib import admin

# Register your models here.
from .models import customer,product, Contact, proimage
admin.site.register(customer)
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(proimage)
