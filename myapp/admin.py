from django.contrib import admin
from myapp.models import *

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Buy)

# Register your models here.
