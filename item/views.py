from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .form import NewItemFormm


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemFormm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemFormm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
<<<<<<< HEAD
    item.delete()

    return redirect('dashboard:index')
=======
<<<<<<< HEAD
    item.delete()

    return redirect('dashboard:index')
=======
    item.delete()
>>>>>>> 1d2d62a68b50d4263e582a7923ad438dbfff09d8
>>>>>>> b28ccd908ac88b9bfce40504e4d132d0e41c1622
