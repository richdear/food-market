from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from .forms import ItemForm
from django.template import loader


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, "food/index.html", context)


def item_details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'food/item_details.html', context)


def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        description = form.cleaned_data['description']
        image_url = form.cleaned_data['image_url']
        new_item = Item(name=name, price=price, description=description, image=image_url)
        new_item.save()
        return redirect("food:index")
    return render(request, "food/add-item.html", {"form": form})


def item(request):
    return HttpResponse("<h1>Fixed in main This is item</h1>")
