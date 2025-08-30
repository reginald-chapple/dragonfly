from django.urls import path, include

from competitions.views import competition_outcome_collection, competition_outcome_detail


urlpatterns = [
    path('competition/outcomes/', include(([
        path('', competition_outcome_collection, name='collection'),
        path('<uuid:pk>/', competition_outcome_detail, name='detail'),
    ], 'competition_outcomes'))),
]