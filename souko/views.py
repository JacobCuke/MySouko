from django.shortcuts import render
from .models import Item
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class ItemListView(ListView):
    model = Item
    template_name = 'souko/home.html'
    context_object_name = 'items'
    paginate_by = 10


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'souko/home.html', context)
