from django.urls import path
from .views import WordNetMatchView, IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', WordNetMatchView.as_view(), name='wordnet_match'),
]
