from django.urls import path
from .views import add_person

urlpatterns = [
    path('add-person/', add_person, name='add_person'),
]
