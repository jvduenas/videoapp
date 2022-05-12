from django.contrib import admin
from .models import Category, Vids, Featured, Events

# Register your models here.
admin.site.register(Vids)
admin.site.register(Featured)
admin.site.register(Events)
admin.site.register(Category)