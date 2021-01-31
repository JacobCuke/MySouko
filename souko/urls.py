from django.urls import path
from . import views
from .views import HomeListView, UserListView, ItemCreateView, ItemUpdateView

urlpatterns = [
    path('', HomeListView.as_view(), name='souko-home'),
    path('mylist/', views.mylist, name='souko-mylist'),
    path('mylist/<str:username>/', UserListView.as_view(), name='user-mylist'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('toggle_completed/<int:pk>/', views.completed, name='item-toggle-completed'),
]