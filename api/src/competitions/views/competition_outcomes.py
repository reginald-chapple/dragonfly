from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from competitions.models import CompetitionOutcome
from competitions.serializers import CompetitionOutcomeSerializer

@api_view(['GET', 'POST'])
def competition_outcome_collection(request):
    if request.method == 'GET':
        outcomes = CompetitionOutcome.objects.all()
        serializer = CompetitionOutcomeSerializer(outcomes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompetitionOutcomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def competition_outcome_detail(request, pk):
    try:
        outcome = CompetitionOutcome.objects.get(pk=pk)
    except CompetitionOutcome.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompetitionOutcomeSerializer(outcome)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompetitionOutcomeSerializer(outcome, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        outcome.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)