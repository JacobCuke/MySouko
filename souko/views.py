from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Item
from datetime import date
from django.http import HttpResponse
from .forms import ItemForm
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


class UserListView(ListView):
    model = Item
    template_name = 'souko/user_list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Item.objects.filter(user=user).order_by('-date_started')


class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'souko/item_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'souko/item_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def completed(request, **kwargs):
    if (request.user.is_authenticated):
        pk = kwargs.get('pk')
        print(pk)
        obj = Item.objects.get(pk=pk)
        owner = obj.user
        if (owner == request.user):
            obj.completed = not obj.completed
            if (obj.completed):
                obj.date_completed = date.today()
                obj.save()
                return HttpResponse(obj.date_completed.strftime("%Y/%m/%d"))
            else:
                obj.date_completed = None
                obj.save()
                return HttpResponse("")
    return HttpResponse("Access Denied")