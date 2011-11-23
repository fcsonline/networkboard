from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.serializers import serialize
from django.utils.functional import curry
from django.db.models.query import QuerySet
from django.db import models
from django.utils import simplejson
from networkboard.models import Node
from django.utils.functional import curry
from django.utils.simplejson import dumps, loads, JSONEncoder

class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        if isinstance(obj, models.Model):
            #do the same as above by making it a queryset first
            set_obj = [obj]
            set_str = serialize('json', set_obj)
            #eliminate brackets in the beginning and the end 
            str_obj = set_str[1:len(set_str)-2]
            return str_obj
        return JSONEncoder.default(self,obj)

# partial function, we can now use dumps(my_dict) instead
# of dumps(my_dict, cls=DjangoJSONEncoder)
dumps = curry(dumps, cls=DjangoJSONEncoder)

def test(request):

    nodes = Node.objects.all()

    return HttpResponse(dumps(nodes))

def home(request):

    nodes = Node.objects.all()

    data = {'test':'hola'}	

    return render_to_response('home.html', data, context_instance=RequestContext(request))

