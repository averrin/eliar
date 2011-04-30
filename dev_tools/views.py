# Create your views here.
from dev_tools.forms import TodoForm
from dev_tools.models import ToDo
from shared import login_required, redirect

@login_required
def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            ToDo(text=form.cleaned_data['text']).save()
    return redirect('index')


@login_required
def todo_del(request, todo_id):
    ToDo.objects.get(pk=todo_id).delete()
    return redirect('index')


@login_required
def todo_done(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    if todo.done:
        todo.done = False
    else:
        todo.done = True
    todo.save()
    return redirect('index')

