from django.urls import path
from .views import TicketsView, create_ticket, check_ticket, buy_ticket, HelloView

urlpatterns = [
    path('', TicketsView.as_view()),
    path('create/', create_ticket, name='create'),
    path('check/', check_ticket, name='check'),
    path('buy/', buy_ticket, name='buy'),
    path('hello/', HelloView.as_view(), name='hello'),
]
