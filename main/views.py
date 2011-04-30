# Create your views here.
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from accounts.views import my_profile
from main.forms import requestInvitation
from main.models import inviteRequest
from shared import render_to, login_required, redirect
from dev_tools.models import ToDo
from dev_tools.forms import TodoForm

@render_to('welcome.html')
def frontend(request):
    if request.subdomain == 'me':
        return my_profile(request)
    else:
        if request.user.is_authenticated() and not request.user.is_anonymous():
            return redirect('index')
        else:
            return {'profile':User.objects.get(pk=1).profile}


@login_required
@render_to('index.html')
def index(request):
    todo = ToDo.objects.all()
    form = TodoForm()
    return {'todo': todo, 'form': form}


@render_to('invitation/request_invite.html')
def request_invite(request):
    if request.method == 'POST':
        form = requestInvitation(data=request.POST)
        if form.is_valid():
            inviteRequest(email=form.cleaned_data['email'], about=form.cleaned_data['about']).save()
            return redirect(request_invite_complete)
        else:
            return {'form': form}
    else:
        form = requestInvitation()
        return {'form': form}


@render_to('invitation/request_invite_complete.html')
def request_invite_complete(request):
    return {}


def my_route(request, url):
    return redirect('http://%s/%s' % (Site.objects.get_current(), url))