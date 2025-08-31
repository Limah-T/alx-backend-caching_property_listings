from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property  # assuming you have a Property model

@cache_page(60 * 15)  # cache for 15 minutes
def property_list(request):
    properties = Property.objects.all().values("id", "name", "price", "location")  
    return JsonResponse({"data":list(properties)}, safe=False)