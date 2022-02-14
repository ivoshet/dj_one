from django.http import HttpResponse

def first_page(request):
    return HttpResponse('hello from python')


