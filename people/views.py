from __future__ import absolute_import
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView

from .forms import PersonForm
from .models import Person

PAGE_SIZE = 2

def list_people(request):
    people_list = Person.objects.all()
    paginator = Paginator(people_list, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        people = paginator.page(page)
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)

    return render(request, 'people/list_people.html', {
        "people": people,
    })

def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "people/person.html", {
        "person": person,
    })

@login_required
def add_person(request):
    instance = Person(user=request.user)
    if request.method == "POST":
        form = PersonForm(instance=instance, data=request.POST)
        if form.is_valid():
            person = form.save()
            return redirect(person)
    elif request.method == "GET":
        form = PersonForm(instance=instance)
    else:
        return HttpResponse(status_code=405)

    return render(request, "people/add_person.html", {
        "form": form,
    })


@login_required
def edit_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id, user=request.user)
    if request.method == "POST":
        form = PersonForm(instance=person, data=request.POST)
        if form.is_valid():
            person = form.save()
            return redirect(person)
    elif request.method == "GET":
        form = PersonForm(instance=person)
    else:
        return HttpResponse(status_code=405)

    return render(request, "people/edit_person.html", {
        "person": person,
        "form": form,
    })
