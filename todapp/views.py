from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from .models import TodoItem
from .models import TAG_CHOICES
from django.http import HttpResponseRedirect


class home(ListView):
    model = TodoItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_choices"] = TAG_CHOICES
        context["print"] = "DFFDF"
        return context


class TodoItemCreateView(CreateView):
    model = TodoItem
    fields = ['todoitem', 'note', 'completed', 'due_date']


class TodoItemUpdateView(UpdateView):
    model = TodoItem
    fields = ['todoitem', 'note', 'completed', 'due_date']


def TodoItemDeleteView(request, pk):
    todo = TodoItem.objects.get(pk = pk)
    todo.delete()
    return redirect("todoapp:home-url")


def updatedone(request, pk):
    item = TodoItem.objects.get(pk = pk)
    if item.completed:
        item.completed = False
    else:
        item.completed = True
    item.save()
    return redirect("todoapp:home-url")
