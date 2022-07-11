from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def pasta_view(request):
    template_name = 'calculator/pasta.html'
    servings = int(request.GET.get('servings', 1))
    pasta = DATA['pasta']

    pasta_servings = {}
    for name, count in pasta.items():
        pasta_serv[name] = count * servings

    context = {
        'pasta': pasta_servings,
    }

    return render(request, template_name, context)


def omlet_view(request):

    template_name = 'calculator/omlet.html'
    servings = int(request.GET.get('servings', 1))
    omlet = DATA['omlet']

    omlet_servings = {}
    for name, count in omlet.items():
        omlet_servings[name] = count * servings

    context = {
        'omlet': omlet_servings,
    }

    return render(request, template_name, context)


def buter_view(request):
    template_name = 'calculator/buter.html'
    servings = int(request.GET.get('servings', 1))
    buter = DATA['buter']

    buter_servings = {}
    for name, count in buter.items():
        buter_servings[name] = count * servings

    context = {
        'buter': buter_servings,
    }

    return render(request, template_name, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
