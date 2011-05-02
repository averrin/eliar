from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseRedirect
from settings import VERSION, STATIC_URL, ASSET_URL
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from main.models import *
from django.utils.translation import ugettext_lazy as _

def	my_context(context):
    '''
    our context processor. Add to dict vars to send in ALL templates.
    '''
    requests=inviteRequest.objects.all().count()
    try:
        inbox_count=context.user.received_messages.filter(read_at__isnull=True, recipient_deleted_at__isnull=True).count()
    except:
        inbox_count=0
    return {
        'VERSION' : VERSION,
        'STATIC' : STATIC_URL,
        'ASSET_URL' : ASSET_URL,
        'HOME' : 'http://%s' % Site.objects.get_current().domain,
        'requests_count':requests,
        'inbox_count':inbox_count,
        'subdomain': context.subdomain
    }

def render_to(template):
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer