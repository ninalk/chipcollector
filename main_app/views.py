from django.shortcuts import render

class Chip:
  def __init__(self, brand, flavor, style, origin):
    self.brand = brand
    self.flavor = flavor
    self.style = style
    self.origin = origin

chips = [
  Chip('SpudLove', 'Sea Salt', 'Thick-Cut', 'Oregon'),
  Chip('Kettle Brand', 'Jalapeno', 'Thick-Cut', 'Oregon'),
  Chip('Boulder Canyon', 'Cheddar Sour Cream', 'Thin & Crispy', 'Pennsylvania')
]


# Create your views here.
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Welcome to ChipCollector!</h1>')

def about(request):
  return render(request, 'about.html')

def chips_index(request):
  return render(request, 'chips/index.html', { 'chips': chips })