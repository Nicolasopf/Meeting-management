''' Create views for the pages. '''
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, CustomUserCreationForm
from rest_framework.authtoken.models import Token
from django.views.generic import CreateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(TemplateView):
    ''' Index page. '''
    template_name = 'meetmanage/index.html'

    def get(self, request, *args, **kwargs):
        ''' Show signup and login form. '''
        if request.user.is_authenticated:
            return redirect('/panel')

        signup_form = CustomUserCreationForm
        login_form = LoginForm
        context = self.get_context_data(**kwargs)
        context['signup_form'] = signup_form
        context['login_form'] = login_form
        return self.render_to_response(context)


class SignUp(CreateView):
    ''' Allow users to signup '''
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        ''' If the form is valid, then: '''
        form.save()
        user = authenticate(
            username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
        login(self.request, user)
        return redirect('/panel')

    def form_invalid(self, form):
        ''' If the form is invalid, then: '''
        messages.error(self.request, form.errors)
        return redirect("/")


class Login(View):
    ''' Allow login for users. '''

    def post(self, request):
        ''' Accept the data sent and login the user. '''
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=user, password=password)
        if not user:
            messages.error(self.request, "Invalid password or username")
            return redirect("/")
        login(self.request, user)
        return redirect('/panel')


class Panel(LoginRequiredMixin, View):
    '''
    Panel for authenticated users.
    As is no needed to use multiple views for login and signup, we can receive
    posts here, so user is always being redirected to panel after login/register.
    '''
    login_url = '/'
    context = {}

    def get(self, request):
        ''' Panel to show the reservations. '''
        user = User.objects.filter(username=request.user).first()
        self.context['token'], created = Token.objects.get_or_create(user=user)
        return render(request, 'meetmanage/panel.html', self.context)


class NewMeeting(LoginRequiredMixin, View):
    ''' For users, can create new meetings. '''
    login_url = '/'

    def get(self, request):
        ''' Show the html to create new meeting by using the api. '''
        user = User.objects.filter(username=request.user).first()
        return render(request, 'meetmanage/new.html')


class Logout(View):
    """ Allow to logout for users. """

    def get(self, request):
        ''' Logout an user '''
        logout(request)
        return redirect('/')
