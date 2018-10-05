from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {
        'event'  : 'PyConES 2018',
        'detail' : 'API in django',
        'requirements': 'django==2.1.2'
    }
    return JsonResponse(data)
    
