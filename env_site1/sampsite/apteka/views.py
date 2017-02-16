from django.http import *

# Create your views here.


def index(request):
    mydict = dict(request.GET.iterlists())
    print mydict.get('dupa')[0]

    return HttpResponse( {'debug': mydict.get('dupa')[0], 'dupa': 5} )
