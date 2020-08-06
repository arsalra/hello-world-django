from django.http import HttpResponse, JsonResponse

def hello(request):
    return HttpResponse('hello')