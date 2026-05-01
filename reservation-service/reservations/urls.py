from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreerReservationView.as_view()),
    path('all/', views.ToutesReservationsView.as_view()),
    path('<int:id>/', views.DetailReservationView.as_view()),
    path('client/<int:clientId>/', views.ReservationsClientView.as_view()),
    path('table/<int:tableId>/', views.ReservationsTableView.as_view()),
]