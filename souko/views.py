from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Item
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class HomeListView(ListView):
    model = Item
    template_name = 'souko/home.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, id=1)
        return Item.objects.filter(user=user).order_by('-date_started')
