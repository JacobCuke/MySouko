from django.shortcuts import render

items = [
    {
        'title': '進撃の巨人 ２５',
        'cover_art': 'aot_25.jpg',
        'series': '進撃の巨人',
        'genre': '漫画',
        'completed': True,
        'date_started': '2020/12/29',
        'date_completed': '2020/12/29'
    },
    {
        'title': 'Fate/Zero １',
        'cover_art': 'fatezero_1.jpg',
        'series': 'Fate/stay night',
        'genre': 'ライトノベル',
        'completed': True,
        'date_started': '2020/12/22',
        'date_completed': '2020/12/27'
    },
    {
        'title': 'Fate/Zero ２',
        'cover_art': 'fatezero_2.jpg',
        'series': 'Fate/stay night',
        'genre': 'ライトノベル',
        'completed': False,
        'date_started': '2020/12/28',
        'date_completed': ''
    },
]

def home(request):
    context = {
        'items': items
    }
    return render(request, 'souko/home.html', context)
