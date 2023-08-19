from django.urls import path
from .views import searchResult, clear_search_history

app_name = 'search'

urlpatterns = [
    path('search/', searchResult, name='searchResult'),
    path('clear_history/', clear_search_history, name='clear_history'),
]