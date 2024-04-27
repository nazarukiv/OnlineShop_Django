from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from goods.models import Products


def catalog(request, category_slug):
    page = request.GET.get('page', 1)

    if category_slug == "all-goods":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(goods, per_page=3)
    current_page = paginator.page(int(page))


    context = {
        'title': 'Catalog',
        'goods': current_page,
        'slug_url': category_slug
    }

    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context)
