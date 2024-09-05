from django.urls import path

from .views import add_link, add_review, detail


app_name = 'link'


urlpatterns = [
    path('add/', add_link, name='add_link'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/add/', add_review, name='add_review'),
]