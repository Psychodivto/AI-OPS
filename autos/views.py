from django.http import JsonResponse
from graphene_django.views import GraphQLView

# Create your views here.

def ping(request):
    return JsonResponse({'status': 'ok'})