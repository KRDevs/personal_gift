from django.shortcuts import render,redirect
from item.models import Category, Item
from .forms import SignupForm

def logout(request):
    return render(request,'core/main.html')
def new_page(request):
    return  render(request,'core/new_page.html')
def index(request):
    items = Item.objects.order_by('-id')[:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })
def about(request):
    return render(request,'core/about.html')
