# Create your views here.
from mish.forms import LinkForm

from shared import *
from models import Link

@render_to('mish.html')
def index(request):
    links=Link.objects.all()
    form=LinkForm()
    if request.method == 'POST':
        form = LinkForm(data=request.POST)
        if form.is_valid():
            form.save()
            form=LinkForm()
    return {'links':links,'form':form}

def del_link(request,link_id=''):
    link=Link.objects.get(pk=link_id)
    link.delete()
    return redirect(index)

