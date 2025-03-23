from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    sort_rule = {
        'name': Phone.objects.all().order_by('name'),
        'min_price': Phone.objects.all().order_by('price'),
        'max_price': Phone.objects.all().order_by('-price'),
    }

    if sort in sort_rule.keys():
        phones = sort_rule[sort]
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = slug.replace('-', ' ')
    phone = Phone.objects.get(name__iregex=rf'{product}')
    context = {
        'phone': phone,
    }
    return render(request, template, context)
