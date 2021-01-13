from django.urls import path
from . import views
from .views import HomeListView, UserListView

urlpatterns = [
    path('', HomeListView.as_view(), name='souko-home'),
    path('mylist/<str:username>/', UserListView.as_view(), name='souko-mylist'),
]