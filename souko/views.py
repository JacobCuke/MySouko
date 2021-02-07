from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item
from .forms import ItemForm
from datetime import date
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class HomeListView(ListView):
    model = Item
    template_name = 'souko/home_list_all.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, id=1)
        return Item.objects.filter(user=user).order_by('-date_started', '-pk')


class HomeListInProgressView(ListView):
    model = Item
    template_name = 'souko/home_list_inprogress.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, id=1)
        return Item.objects.filter(user=user, completed=False).order_by('-date_started', '-pk')


class HomeListCompletedView(ListView):
    model = Item
    template_name = 'souko/home_list_completed.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, id=1)
        return Item.objects.filter(user=user, completed=True).order_by('-date_completed', '-pk')


class UserListView(ListView):
    model = Item
    template_name = 'souko/user_list_all.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Item.objects.filter(user=user).order_by('-date_started', '-pk')


class UserListInProgressView(ListView):
    model = Item
    template_name = 'souko/user_list_in_progress.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Item.objects.filter(user=user, completed=False).order_by('-date_started', '-pk')


class UserListCompletedView(ListView):
    model = Item
    template_name = 'souko/user_list_completed.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Item.objects.filter(user=user, completed=True).order_by('-date_completed', '-pk')


class ItemCreateView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = 'souko/item_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'souko/item_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.user:
            return True
        return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/mylist/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.user:
            return True
        return False


def mylist(request):
    if (request.user.is_authenticated):
        return redirect('user-mylist', username=request.user.username)
    else:
        return redirect('login')


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