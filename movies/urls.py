from django.urls import path
from . import views
from .views import movie_list, theater_list
urlpatterns = [
    path('', movie_list, name='movie_list'), 
    path('<int:movie_id>/theaters/', theater_list, name='theater_list'),
    path('theater/<int:theater_id>/seats/', views.book_seats, name='seat_list'),
    path('theater/<int:theater_id>/seats/', views.book_seats, name='book_seats'),



]


