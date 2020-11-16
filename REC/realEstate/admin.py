from django.contrib import admin
from .models import Customer
from .models import Property

# Registering the customer model


class CustomerList(admin.ModelAdmin):
    list_display = ('fname','lname','city', 'phone')
    list_filter = ('fname', 'city')
    search_fields = ('fname', 'city')
    ordering = ['fname']


admin.site.register(Customer)


# Registering the property model

class PropertyList(admin.ModelAdmin):
    list_display = ('type', 'purpose', 'image')
    list_filter = ('type', 'price')
    search_fields = ('type', 'price', 'purpose')
    ordering = ['type']


admin.site.register(Property)

