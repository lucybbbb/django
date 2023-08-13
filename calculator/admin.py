from django.contrib import admin

# Register your models here.


from .models import *

# Now, Register the models here.

class foodAdmin(admin.ModelAdmin):
    class Meta:
        model=Fooditem
    list_display=['name']
    list_filter=['name']


admin.site.register(UserFooditem)
admin.site.register(Category)
admin.site.register(Fooditem,foodAdmin)
admin.site.register(Customer)