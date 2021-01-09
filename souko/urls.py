from django.urls import path
from . import views
from .views import ItemListView

urlpatterns = [
    path('', ItemListView.as_view(), name='souko-home'),
]