from django.contrib import admin

# Register your models here.

from .models import Food,ProfileCalorie,PostFood
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
admin.site.register(Food)
admin.site.register(ProfileCalorie)