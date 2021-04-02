from django.db import models
from django.urls import reverse
from datetime import date

REVIEWS = (
  ('P', 'Poor'),
  ('O', 'Okay'),
  ('G', 'Good'),
  ('F', 'Fantastic')
)

# Create your models here.
class Store(models.Model):
  name = models.CharField(max_length=50)
  size = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('stores_detail', kwargs={'pk': self.id})



class Chip(models.Model):
  brand = models.CharField(max_length=100)
  flavor = models.CharField(max_length=100)
  style = models.TextField(max_length=250)
  origin = models.CharField(max_length=100)
  stores = models.ManyToManyField(Store)

  def __str__(self):
    return self.brand

  def get_absolute_url(self):
    return reverse('detail', kwargs={'chip_id': self.id})

  def ate_too_much(self):
    return self.reviews_set.filter(date=date.today()).count() >= len(REVIEWS)


class Reviews(models.Model):
  date = models.DateField('review date')
  review = models.CharField(
    max_length=1,
    # add 'choices' field option
    choices=REVIEWS,
    # set default to 'G'
    default=REVIEWS[2][0]
  )

  chip = models.ForeignKey(Chip, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_review_display()} on {self.date}"

  class Meta:
    ordering = ['-date']