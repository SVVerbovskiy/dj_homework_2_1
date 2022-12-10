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
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cake': {
        'шоколад, плитка': 0.5,
        'сахар, ч.л': 1,
        'сметана, ч.л': 0.5,
        'клубника, шт': 5
    },
    'meatballs': {
        'фарш, г': 100,
        'рис, г': 20,
        'мука, ст': 0.3,
        'соль, ч.л.': 0.5
    }
}


def recepies(request, recipe_name):
    if recipe_name in DATA.keys():
        servings = request.GET.get('servings', 1)
        ingredients = {}
        for ingredient in DATA[recipe_name]:
            ingredients[ingredient] = round(DATA[recipe_name][ingredient] * int(servings), 2)
        context = {
            'recipe': ingredients
        }
    else:
        context = {}

    return render(request, template_name='index.html', context=context)


def home(request):
    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}
    return render(request, template_name='home.html', context=context)
