from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Workout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
	context = {
        'workouts': Workout.objects.all()
    }
	return render(request, 'fitlog/home.html', context)

def enter(request):
	return render(request, 'fitlog/enter.html')

class WorkoutListView(ListView):
	model = Workout
	template_name = 'fitlog/home.html'
	context_object_name = 'workouts'
	paginate_by = 3

	def get_queryset(self):
		return Workout.objects.filter(person=self.request.user)

class AllListView(ListView):
	model = Workout
	template_name = 'fitlog/all.html'
	context_object_name = 'workouts'
	paginate_by = 5

	def get_queryset(self):
		return Workout.objects.filter(person=self.request.user)

class WorkoutDetailView(DetailView):
	model = Workout


class WorkoutCreateView(LoginRequiredMixin, CreateView):
	model = Workout
	fields = ['date_of', 'body_part', 'exercise', 'weight', 'sets', 'reps']
	succes_url = reverse_lazy('fit-home')


	def get_form(self, form_class = None):
		from django.forms.widgets import SelectDateWidget
		form = super(WorkoutCreateView, self).get_form(form_class)
		form.fields['date_of'].widget = SelectDateWidget()
		return form

	def form_valid(self,form):
		form.instance.person = self.request.user
		super().form_valid(form)
		messages.success(self.request, "Workout Logged.")
		return HttpResponseRedirect(reverse_lazy('fit-home'))



class WorkoutUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Workout
	fields = ['date_of', 'body_part', 'exercise', 'weight', 'sets', 'reps']

	def get_form(self, form_class = None):
		from django.forms.widgets import SelectDateWidget
		form = super(WorkoutUpdateView, self).get_form(form_class)
		form.fields['date_of'].widget = SelectDateWidget()
		return form

	def form_valid(self,form):
		form.instance.person = self.request.user
		super().form_valid(form)
		messages.success(self.request, "Workout Updated.")
		return HttpResponseRedirect(reverse_lazy('fit-home'))

	def test_func(self):
		workout = self.get_object()
		if self.request.user == workout.person:
			return True
		return False

class WorkoutDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Workout

	def test_func(self):
		workout = self.get_object()
		if self.request.user == workout.person:
			return True
		return False

	success_url = reverse_lazy('fit-home')
