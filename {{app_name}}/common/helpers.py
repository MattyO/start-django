import json
import types
from django.http import HttpResponse

def jsonify(an_object):
    return HttpResponse(json.dumps(an_object), content_type="application/json")

def resolve_http_method(request, methods):
    '''Thinking this method is pasted a list of methods or the dictonary returned from the python core function locals.  However any dictonary with function objects will do which gives it a nice amount of scoping and configurablity
    '''
    if isinstance(methods, types.ListType):
        methods = { a_function.__name__ : a_function for a_function in methods }
    if request.method.lower() not in methods.keys():
        return HttpResponse(status=501)

    return methods[request.method.lower()]()
