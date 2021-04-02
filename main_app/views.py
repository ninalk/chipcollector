from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chip, Store
from .forms import ReviewForm


# Create your views here.
class ChipCreate(CreateView):
  model = Chip
  fields = '__all__'

class ChipUpdate(UpdateView):
  model = Chip
  fields = ['flavor', 'style', 'origin']

class ChipDelete(DeleteView):
  model = Chip
  success_url = '/chips/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def chips_index(request):
  chips = Chip.objects.all()
  return render(request, 'chips/index.html', { 'chips': chips })

def chips_detail(request, chip_id):
  chip = Chip.objects.get(id=chip_id)
  # get stores the chip does not have
  stores_chip_is_not_sold = Store.objects.exclude(id__in = chip.stores.all().values_list('id'))

  review_form = ReviewForm()
  # instantiate ReviewForm to be rendered in the template
  return render(request, 'chips/detail.html', { 
    'chip': chip, 
    'review_form': review_form,
    'stores': stores_chip_is_not_sold 
  })

def assoc_store(request, chip_id, store_id):
  Chip.objects.get(id=chip_id).stores.add(store_id)
  return redirect('detail', chip_id=chip_id)

def unassoc_store(request, chip_id, store_id):
  Chip.objects.get(id=chip_id).stores.remove(store_id)
  return redirect('detail', chip_id=chip_id)

def add_review(request, chip_id):
  # create a ModelForm instance using the data in request.POST
  form = ReviewForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it has the chip_id assigned
    new_review = form.save(commit=False)
    new_review.chip_id = chip_id
    new_review.save()
  return redirect('detail', chip_id=chip_id)

class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name', 'size']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores/' 