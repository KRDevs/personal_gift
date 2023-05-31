from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item,Category
from .forms import NewItemForm, EditItemForm

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    is_author = request.user == item.author
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'is_author': is_author,
        'related_items': related_items
    })


def items(request):
    items = Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)
    query = request.GET.get('query', '')
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        items=items.filter(category_id=category_id)
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories':categories,
        'category_id':int(category_id),
    })


@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
        return render(request, 'item/new_item.html', {
            'form': form,
            'title': 'Yangi mahsulot qoshish'
        })
from django.shortcuts import render
from django import forms

class NumberForm(forms.Form):
    son = forms.DecimalField()
def my_view(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            son = form.cleaned_data['son']
            # Tasdiqlangan son bilan qo'shimcha ishlarni bajaring
            return render(request, 'muaffaqiyat.html', {'son': son})
    else:
        form = NumberForm()

    return render(request, 'forma.html', {'form': form})
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, author=request.user)
    item.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, author=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request, 'item/new_item.html', {
        'form': form,
        'title': 'Ozgartirish'
    })
