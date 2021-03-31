from django.contrib import admin
from .models import Chip, Reviews
# Register your models here.

admin.site.register(Chip)

# register the new Reviews Model
admin.site.register(Reviews)
