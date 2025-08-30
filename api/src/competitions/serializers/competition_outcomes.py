from rest_framework import serializers
from competitions.models import CompetitionOutcome

class CompetitionOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionOutcome
        fields = '__all__'