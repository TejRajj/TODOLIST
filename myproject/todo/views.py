from django.shortcuts import render

# Create your views here.
from .models import Todo
def index(request):
    todo_list = Todo.objects.order_by('id')
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)
