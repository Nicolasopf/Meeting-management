''' Create views for the pages. '''
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, SignUpForm
from rest_framework.authtoken.models import Token


def index(request):
    ''' Root page '''
    context = {}
    context['login'] = LoginForm()
    context['signup'] = SignUpForm()
    if request.user.is_authenticated:
        return redirect("/panel")
    return render(request, 'meetmanage/index.html', context)


class Panel(View):
    '''
    Panel for authenticated users.
    As is no needed to use multiple views for login and signup, we can receive
    posts here, so user is always being redirected to panel after login/register.
    '''
    context = {}

    def get(self, request):
        ''' Panel to show the reservations. '''
        if not request.user.is_authenticated:
            return redirect("/")

        user = User.objects.filter(username=request.user).first()
        self.context['token'], created = Token.objects.get_or_create(user=user)
        return render(request, 'meetmanage/panel.html', self.context)

    def post(self, request):
        ''' When log in or sign up.'''
        post = request.POST

        # Basic validation to check if data sent is correct:
        if 'password' not in post:
            messages.error(request, "Insert a password.")
            return redirect('/')
        elif 'username' not in post:
            messages.error(request, "Insert an user")
            return redirect('/')

        if 'email' not in post:
            login_form = LoginForm(post)
            if login_form and login_form.is_valid():
                login_data = login_form.data
                username = login_data['username']
                password = login_data['password']

                user = authenticate(username='a', password='1234')
                print(user)
                if not user:  # If credentials wrong.
                    messages.error(request, "Incorrect credentials.")
                    return redirect('/')

                login(request, user)
                # Needs to be replaced for the panel html
                self.context['token'], created = Token.objects.get_or_create(
                    user=user)
                return render(request, 'meetmanage/panel.html', self.context)

        # Email exists so try to signup:
        signup = SignUpForm(post)
        if signup and signup.is_valid():
            signup_data = signup.data
            username = signup_data['username']
            first_name = signup_data['first_name']
            last_name = signup_data['last_name']
            email = signup_data['email']
            password = signup_data['password']

            if User.objects.filter(username=username).first():
                messages.error(request, "This username is already taken")
                return redirect('/')
            elif User.objects.filter(email=email).first():
                messages.error(request, "This email is already taken")
                return redirect('/')

            user = User.objects.create_user(
                username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            user.save()
            login(request, user)

            self.context['token'], created = Token.objects.get_or_create(
                user=user)

        # Needs to be replaced for the panel html
        return render(request, 'meetmanage/panel.html', self.context)
