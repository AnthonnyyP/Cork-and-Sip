from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    return render(request, 'guests/detail.html', {'guest': guest})

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
