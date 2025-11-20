from django.urls import path
from .views import save_person

urlpatterns = [
    path('save-person/', save_person, name='save-person'),
]
