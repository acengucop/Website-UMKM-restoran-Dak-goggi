from django.contrib import admin
from .models import MenuItem, Promo, Category, MiniItem
from .models import Testimonial

admin.site.register(MenuItem)
admin.site.register(Promo)
admin.site.register(Category)
admin.site.register(MiniItem)
admin.site.register(Testimonial)
