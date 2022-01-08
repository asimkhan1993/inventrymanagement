
from django.shortcuts import render
from .forms import ItemRegistration
from .models import Item

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        fm = ItemRegistration(request.POST)
        if fm.is_valid():
            pnam = fm.cleaned_data['product_name']
            pnum = fm.cleaned_data['product_number']
            pt = fm.cleaned_data['product_type']
            pd = fm.cleaned_data['product_description']
            pc = fm.cleaned_data['product_category']
            st = fm.cleaned_data['status']
            um = fm.cleaned_data['unit_measure']
            pty = fm.cleaned_data['packing_type']
            reg = Item(product_name=pnam, product_num=pnum, product_type=pt,
                       product_description=pd, product_category=pc,
                       status=st, unit_measure=um, packing_type=pty)
            reg.save()
            fm = ItemRegistration()
    else:
        fm = ItemRegistration()
    ite = Item.objects.all()
    return render(request, 'inventory/base.html', {'form':fm, 'it':ite})
