from django.contrib import admin
from .models import Chip, Reviews, Store
# Register your models here.

admin.site.register(Chip)

# register the new Reviews Model
admin.site.register(Reviews)

# register the new Store Model
admin.site.register(Store)
