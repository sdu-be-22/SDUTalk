from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from .forms import LoginUserForm, RegisterUserForm

from django.apps import apps


class BlogListView(ListView):
    model = apps.get_model('blog', 'Posts')
    template_name = 'main/index.html'
    context_object_name = 'posts'

    ordering = ['-date']

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

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

