from django.urls import path
from . import views
from .views import (
    HomeListView,
    HomeListInProgressView,
    HomeListCompletedView, 
    UserListView,
    UserListInProgressView,
    UserListCompletedView,
    ItemCreateView, 
    ItemUpdateView, 
    ItemDeleteView
)

urlpatterns = [
    path('', HomeListView.as_view(), name='souko-home'),
    path('about/', views.about, name='souko-about'),
    path('home/inprogress/', HomeListInProgressView.as_view(), name='souko-home-inprogress'),
    path('home/completed/', HomeListCompletedView.as_view(), name='souko-home-completed'),
    path('mylist/', views.mylist, name='souko-mylist'),
    path('mylist/<str:username>/', UserListView.as_view(), name='user-mylist'),
    path('mylist/<str:username>/inprogress/', UserListInProgressView.as_view(), name='user-mylist-inprogress'),
    path('mylist/<str:username>/completed/', UserListCompletedView.as_view(), name='user-mylist-completed'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('toggle_completed/<int:pk>/<int:offset>/', views.completed, name='item-toggle-completed'),
]