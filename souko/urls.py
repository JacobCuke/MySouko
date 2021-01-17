from django.urls import path
from . import views
from .views import HomeListView, UserListView, ItemCreateView

urlpatterns = [
    path('', HomeListView.as_view(), name='souko-home'),
    path('mylist/<str:username>/', UserListView.as_view(), name='souko-mylist'),
    path('item/new/', ItemCreateView.as_view(), name='souko-create'),
    path('toggle_completed/<int:pk>/', views.completed, name='souko-toggle-completed'),
]