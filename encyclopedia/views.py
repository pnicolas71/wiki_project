from django.shortcuts import render

from django import forms

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from . import util

import random

import markdown2


class CreateEntryForm(forms.Form):
    title = forms.CharField(label="Entry Title", widget=forms.TextInput(
        attrs={'placeholder': 'Enter a title'}))
    content = forms.CharField(label="Entry Details", widget=forms.Textarea(
        attrs={"placeholder": "Enter a Entry details", "rows": 20, "cols": 90}))


class EditEntryForm(forms.Form):
    edit_title = forms.CharField(label="Entry Title", widget=forms.TextInput(
        attrs={'placeholder': 'Enter a title'}))
    edit_content = forms.CharField(label="Entry Details", widget=forms.Textarea(
        attrs={"placeholder": "Enter a Entry details", "rows": 20, "cols": 90}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})


def entry_list(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})


def show_entry(request, name):
    entry = util.get_entry(name)

    if entry == None:
        error_message = "The requested Entry was not found"
        return render(request, "encyclopedia/error.html", {
            "error_message": error_message
        })
    else:
        return render(request, "encyclopedia/show_entry.html", {
            "name": name,
            "entry": markdown2.markdown(entry),
        })


def edit_entry(request, name):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            entry_title = form.cleaned_data["edit_title"]
            entry_content = form.cleaned_data["edit_content"]
            util.save_entry(entry_title, entry_content)
            return render(request, "encyclopedia/show_entry.html", {
                "name": entry_title,
                "entry": markdown2.markdown(entry_content),
            })
    else:
        entry = util.get_entry(name)
        if entry == None:
            error_message = "This Entry doesn't exist and can't be edited"
            return render(request, "encyclopedia/error.html", {
                "error_message": error_message
            })
        else:
            form = EditEntryForm(
                initial={'edit_title': name, 'edit_content': entry})
            return render(request, "encyclopedia/edit_entry.html", {
                "form": form,
                "name": name,
                "entry": entry,
            })


def create_entry(request):
    if request.method == "POST":
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            entry_title = form.cleaned_data["title"]
            entry_content = form.cleaned_data["content"]
            entries = util.list_entries()
            check = False
            for entry in entries:
                if entry_title.lower() == entry.lower():
                    title = entry
                    check = True
                    error_message = "This entry already exists"
                    return render(request, "encyclopedia/error.html", {
                        "error_message": error_message,
                    })
            if not check:
                util.save_entry(entry_title, '# ' +
                                entry_title + "\n \n"+entry_content)
                return HttpResponseRedirect('wiki/'+entry_title)
        else:
            return render(request, "encyclopedia/create_entry.html", {
                "form": form
            })
    return render(request, "encyclopedia/create_entry.html", {
        "form": CreateEntryForm()
    })


def search_entry(request):
    if request.method == "POST":
        data = request.POST.copy()
        search = request.POST.get('q')
        founds = []
        found = ''
        pages = util.list_entries()
        for page in pages:
            if search == page:
                found = search
            if search.lower() in page.lower():
                founds.append(page)

        if found:
            entry = util.get_entry(found)
            return HttpResponseRedirect('wiki/'+search)
            # return render(request, "encyclopedia/show_entry.html", {
            #     "name": search,
            #     "entry": markdown2.markdown(entry),
            # })
        elif len(founds):
            return render(request, "encyclopedia/index.html", {
                "entries": founds
            })
        else:
            error_message = "The requested Entry or any Entry that contains this string were not found"
            return render(request, "encyclopedia/error.html", {
                "error_message": error_message,
            })
    else:
        return render(request, "encyclopedia/index.html")


def show_random(request):
    liste = util.list_entries()
    rand = random.choice(liste)
    entry = util.get_entry(rand)
    return HttpResponseRedirect('wiki/'+rand)
