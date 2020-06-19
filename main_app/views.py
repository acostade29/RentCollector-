from django.shortcuts import render

# Add the following import
# from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Property
# Add the Cat class & list and view function below the imports


# Define the home view
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def properties_index(request):
  properties = Property.objects.all()
  return render(request, 'properties/index.html', {'properties': properties})

def properties_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'properties/detail.html', {'property': property})


class PropertyCreate(CreateView):
  model = Property
  fields = '__all__'
