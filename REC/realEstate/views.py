from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import permission_required
from .utils import render_to_pdf
from django.template.loader import get_template
now = timezone.now()


def getActiveEvent():
    activeEvent = Property.objects.filter(event_end_date__isnull=True)
    return activeEvent


# Creating our view, it is a class based view
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = render_to_pdf('pdf.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


def home(request):
    return render(request, 'realEstate/home.html', {'realEstate': home})


# Customer_List
@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'realEstate/customer_list.html', {'customers': customer})


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'realEstate/customer_list.html', {'customers': customer})

    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'realEstate/customer_edit.html', {'form': form})


# customer_delete
@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('realEstate:customer_list')


# customer_Add
@login_required
def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'realEstate/customer_list.html',
                          {'customers': customer})
    else:
        form = CustomerForm()
        # print("Else")
    return render(request, 'realEstate/customer_new.html', {'form': form})


# property_list
@login_required
def property_list(request):
    propertys = Property.objects.filter(created_date__lte=timezone.now())
    return render(request, 'realEstate/property_list.html',
                  {'propertys': propertys})


# property_edit
@login_required
def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        # update
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.updated_date = timezone.now()
            property.save()
            propertys = Property.objects.filter(created_date__lte=timezone.now())
            return render(request, 'realEstate/property_list.html',
                          {'propertys': propertys})
    else:
        # edit
        form = PropertyForm(instance=property)
    return render(request, 'realEstate/property_edit.html', {'form': form})


# property_delete
@login_required
def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    property.delete()
    return redirect('realEstate:property_list')


# Property_Add
@login_required
def property_new(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.created_date = timezone.now()
            property.save()
            propertys = Property.objects.filter(created_date__lte=timezone.now())
            return render(request, 'realEstate/property_list.html',
                          {'propertys': propertys})
    else:
        form = PropertyForm()
        # print("Else")
    return render(request, 'realEstate/property_new.html', {'form': form})


@login_required
def property_summary_pdf(request):
    global propertys
    propertys = Property.objects.filter(created_date__lte=timezone.now())
    context = {'property': propertys,}
    template = get_template('realEstate/property_summary_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('realEstate/property_summary_pdf.html', context)
    return pdf


@permission_required('is_superuser')
def admin_home(request):

        return render(request, 'realEstate/admin_home.html',
                      {'admin': admin_home})



