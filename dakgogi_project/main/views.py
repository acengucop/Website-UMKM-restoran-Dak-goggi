from django.shortcuts import render
from .models import MenuItem, Category, Promo, MiniItem, Testimonial

def homepage(request):
    categories = Category.objects.all()
    promos = Promo.objects.all()

    # Menu utama per kategori
    menu_by_category = {
        category.id: MenuItem.objects.filter(category=category)
        for category in categories
    }

    # Mini Items
    mini_items_makanan = MiniItem.objects.filter(item_type='makanan')
    mini_items_minuman = MiniItem.objects.filter(item_type='minuman')

    # Testimonials
    testimonials = Testimonial.objects.all()

    context = {
        'categories': categories,
        'promos': promos,
        'menu_by_category': menu_by_category,
        'mini_items_makanan': mini_items_makanan,
        'mini_items_minuman': mini_items_minuman,
        'testimonials': testimonials,
    }

    return render(request, 'homepage.html', context)
