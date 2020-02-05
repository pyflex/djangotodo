from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, "Item has been added to list.")
            return render(request, 'index.html', {'all_items': all_items})


    else:

        all_items = List.objects.all
        return render(request, 'index.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, "Item has been deleted from list.")
    return redirect('index')



def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    if item.completed:
        item.completed = False
        item.save()
        messages.success(request, "Item has been uncrossed.")
    else:
        item.completed = True
        item.save()
        messages.success(request, "Item has been crossed off.")

    return redirect('index')



def edit(request, list_id):
    if request.method == "POST":
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item has been edited.")
            return redirect('index')

    else:
        try:
            item = List.objects.get(pk=list_id)
        except Exception:
            return render(request, 'edit.html', {})
        return render(request, 'edit.html', {"item": item})


