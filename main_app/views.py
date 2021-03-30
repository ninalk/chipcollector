from django.shortcuts import render
from .models import Chip


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chips_index(request):
  chips = Chip.objects.all()
  return render(request, 'chips/index.html', { 'chips': chips })

def chips_detail(request, chip_id):
  chip = Chip.objects.get(id=chip_id)
  return render(request, 'chips/detail.html', { 'chip': chip })