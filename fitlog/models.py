from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse



class Workout(models.Model):
    muscles = [
        ('Chest', 'Chest'),
        ('Legs', 'Legs'),
        ('Arms', 'Arms'),
        ('Back', 'Back'),
        ('Core', 'Core')
    ]
    date_of = models.DateField(auto_now=False,default=date.today)
    updated_at = models.DateTimeField(auto_now=True)
    body_part = models.CharField(choices=muscles, max_length=5)
    person = models.ForeignKey(User, on_delete = models.CASCADE)
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    exercise = models.CharField(max_length=100)
    sets = models.IntegerField(validators=[MinValueValidator(1)])
    reps = models.IntegerField(validators=[MinValueValidator(1)])


    def __str__(self):
        return self.body_part

    class Meta:
        ordering = ["-date_of"]

    def get_absolute_url(self):
        return reverse('log-detail', kwargs = {'pk': self.pk})
