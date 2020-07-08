from django.shortcuts import render

from django import forms

from django.http import HttpResponse

from . import util


class CreateEntryForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})


def entry_list(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()})


def show_entry(request, name):
    entry = util.get_entry(name)
    if entry is None:
        error_message = "the requested Entry was not found"
    else:
        error_message = ''
    return render(request, "encyclopedia/show_entry_view.html", {
        "name": name,
        "entry": entry,
        "error_message": error_message,
    })


def search_entry(request):
    if request.method == "POST":
        search = request.POST.get('q')
        founds = []
        found = ''
        pages = util.list_entries()
        for page in pages:
            if search == page:
                found = search
            if search.lower() in page.lower():
                founds.append(page)

        if not found:
            return render(request, "encyclopedia/index.html", {
                "entries": founds
            })
        else:
            entry = util.get_entry(found)
            return render(request, "encyclopedia/show_entry_view.html", {
                "name": search,
                "entry": entry,
            })

    else:
        return render(request, "encyclopedia/index.html")


def random_page(request):
    return HttpResponse('<h1>This is the ramdom page</h1>')
