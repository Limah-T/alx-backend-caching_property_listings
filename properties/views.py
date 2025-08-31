from .models import Property
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
class PropertyView(ModelViewSet):
    queryset = Property.objects.all()

    @cache_page(60 * 15)
    def list(self, request, *args, **kwargs):
        properties = Property.objects.all().values("id", "name", "price", "location")  
        return JsonResponse(list(properties), safe=False)

