from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . import models
from . import serializers


@csrf_exempt
def competition_list(request):
    """
    List all competitions, or create a new competition.
    """
    if request.method == 'GET':
        snippets = models.Competition.objects.all()
        serializer = serializers.CompetitionSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.CompetitionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
