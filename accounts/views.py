# Create your views here.
from django.contrib.auth.models import User
from django.http import Http404

from shared import render_to

@render_to('accounts/profile.html')
def view_profile(request, user_id):
    try:
        profile_user = User.objects.get(pk=user_id)
        profile = profile_user.profile
    except Exception:
        raise Http404
    return {'profile': profile, 'profile_user': profile_user}

@render_to('accounts/profile.html')
def my_profile(request):
    profile_user = User.objects.get(pk=1)
    profile = profile_user.profile
    return {'profile': profile, 'profile_user': profile_user}

