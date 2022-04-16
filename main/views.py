from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from .forms import LoginUserForm

from django.apps import apps
from .forms import UserRegisterForm

class BlogListView(ListView):
    model = apps.get_model('blog', 'Posts')
    template_name = 'main/index.html'
    context_object_name = 'posts'

    ordering = ['-date']

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are able now to log in!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        results = apps.get_model('blog', 'Posts').objects.filter(title__contains = searched)
        return render(request, 'main/search.html', {'searched' : searched, 'results' : results})
    else:
        return render(request, 'main/search.html', {})