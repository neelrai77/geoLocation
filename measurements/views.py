from django.shortcuts import render,get_object_or_404
from .models import Measurement
from .forms import MeasurementModelForm

# Create your views here.
def calculate_distance_view(request):
    obj=get_object_or_404(Measurement,id=1)
    form = MeasurementModelForm(request.POST or None)

    if form.is_valid():
        instance= form.save(commit=False)
        instance.destination= form.cleaned_data.get('destination')
        instance.location='San francisco'
        instance.distance=5000.00
        instance.save()
    context={
        'distance':obj,
        'form':form,
        
    }
    return render(request, 'measurements/main.html',context)