# Create your views here.

from shared import render_to

@render_to('blog/index.html')
def blog_index(request):
    return {}
