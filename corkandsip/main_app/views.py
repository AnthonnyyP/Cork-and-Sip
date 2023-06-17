from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guest
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    id_list = guest.wines.all().values_list('id')
    wines_guest_doesnt_have = Wine.objects.exclude(id__in = id_list)
    tasting_form = TastingForm()
    return render(request, 'guests/detail.html', {
        'guest': guest , 
        'feeding_form': feeding_form,
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
    fields = ['user_name', 'user_email', 'user_phone']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GuestUpdate(LoginRequiredMixin, UpdateView):
    model = Guest
    fields = ['user_email', 'user_phone']


class GuestDelete(LoginRequiredMixin, DeleteView):
    model = Guest
    success_url = '/guests'

@login_required
def add_tasting(request, guest_id):
    form = TastingForm(request.POST)
    if form.is_valid():
        new_tasting = form.save(commit = False)
        new_tasting.guest_id = guest_id
        new_tasting.save()
    return redirect('detail', guest_id = guest_id)

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
def add_to_cellar():
    pass
@login_required
def remove_from_cellar():
    pass