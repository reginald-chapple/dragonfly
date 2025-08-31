from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

@permission_classes([AllowAny])
def test_view(request):
    return JsonResponse({'message': 'This is a test view'})