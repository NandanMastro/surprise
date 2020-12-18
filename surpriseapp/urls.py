from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/<int:surprise_id>', views.show_surprise, name = 'show_surprise'),
]
