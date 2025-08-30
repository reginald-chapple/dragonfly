from django.urls import path, include

urlpatterns = [
    path('', include('competitions.urls.competition_outcomes')),
]