# Create your views here.

from shared import render_to

@render_to('portfolio/index.html')
def view_portfolio(request):
    return {}
