from django.urls import path
from . import views
from .views import (WorkoutListView, WorkoutCreateView, AllListView,
WorkoutDetailView, WorkoutUpdateView, WorkoutDeleteView)

urlpatterns = [
	path('',views.enter, name = 'fit-enter'),
	path('home/',WorkoutListView.as_view(), name = 'fit-home'),
	path('all/',AllListView.as_view(), name = 'all'),
	path('log/new',WorkoutCreateView.as_view(), name = 'log-create'),
	path('log/<int:pk>/',WorkoutDetailView.as_view(), name = 'log-detail'),
	path('log/<int:pk>/update',WorkoutUpdateView.as_view(), name = 'log-update'),
	path('log/<int:pk>/delete',WorkoutDeleteView.as_view(), name = 'log-delete')
]
