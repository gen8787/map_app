from django.shortcuts import render, redirect
from .models import Tour, Leg
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# ---- C R E A T E   T O U R
class TourCreateView(LoginRequiredMixin, CreateView):
    model = Tour
    template_name = 'tours/new_tour.html'
    fields = ('name', 'description')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


# ---- A L L   T O U R S
class TourListView(ListView):
    model = Tour
    template_name = "tours/all_tours.html"
    context_object_name = "tours"


# ---- O N E   T O U R
class TourDetailView(DetailView):
    model = Tour
    template_name = 'tours/one_tour.html'
    fields = ('distance', 'vertical', 'rate')


# ---- U P D A T E   T O U R
class TourUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tour
    template_name = 'tours/edit_tour.html'
    fields = ('name', 'description', 'completed')

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


# ---- D E L E T E   T O U R
class TourDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tour
    template_name = 'tours/delete_tour.html'
    success_url = reverse_lazy('all_tours')

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


def add_leg(request, pk):
    description = request.POST['description']
    distance = request.POST['distance']
    vertical = request.POST['vertical']
    rate = request.POST['rate']
    time = 0

    Leg.objects.create(
        tour=Tour.objects.get(id=pk),
        description=description,
        distance=distance,
        vertical=vertical,
        rate=rate,
        time=time,
        creator=request.user)

    return redirect('/')
