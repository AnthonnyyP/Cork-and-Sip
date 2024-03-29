from django.shortcuts import render, redirect
# CRUD Views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# User Creation & Sign Up
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Guest, Wine
from .forms import TastingForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def guests_index(request):
    guests = Guest.objects.filter(user=request.user)
    return render(request, 'guests/index.html',
                  {'guests': guests})


@login_required
def guests_detail(request, guest_id):
    guest = Guest.objects.get(id=guest_id)
    id_list = guest.wine.all().values_list('id')
    wines_guest_doesnt_have = Wine.objects.exclude(id__in=id_list)
    tasting_form = TastingForm()
    return render(request, 'guests/detail.html', {
        'guest': guest,
        'tasting_form': tasting_form,
        'wines': wines_guest_doesnt_have
    })


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class GuestCreate(LoginRequiredMixin, CreateView):
    model = Guest
    fields = ['username', 'user_Email', 'user_Phone']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GuestUpdate(LoginRequiredMixin, UpdateView):
    model = Guest
    fields = ['user_Email', 'user_Phone']


class GuestDelete(LoginRequiredMixin, DeleteView):
    model = Guest
    success_url = '/guests'


@login_required
def add_tasting(request, guest_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit=False)
        new_tasting.guest_id = guest_id
        new_tasting.save()
    return redirect('detail', guest_id=guest_id)


class WineList(LoginRequiredMixin, ListView):
    model = Wine


class WineDetail(LoginRequiredMixin, DetailView):
    model = Wine


class WineCreate(LoginRequiredMixin, CreateView):
    model = Wine
    fields = '__all__'


class WineUpdate(LoginRequiredMixin, UpdateView):
    model = Wine
    fields = '__all__'


class WineDelete(LoginRequiredMixin, DeleteView):
    model = Wine
    success_url = '/wines'


@login_required
def add_to_cellar(request, guest_id, wine_id):
    Guest.objects.get(id=guest_id).wine.add(wine_id)
    return redirect('detail', guest_id=guest_id)


@login_required
def remove_from_cellar(request, guest_id, wine_id):
    Guest.objects.get(id=guest_id).wine.remove(wine_id)
    return redirect('detail', guest_id=guest_id)
