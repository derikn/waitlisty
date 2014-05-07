from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from waitlisty.forms import ChildForm, ParentForm
from waitlisty.models import Child, Parent, User
from django.utils.decorators import method_decorator

import models

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
		
class AddChild(LoginRequiredMixin, CreateView):
	form_class = ChildForm
	model = Child	
	def form_valid(self, form):
		child = form.save(commit=False)
		child.created_by = self.request.user
		child.save()
		return redirect('/waitlisty/')
		
	def get_success_url(self):
		return reverse('/waitlisty/')

class AddParent(LoginRequiredMixin, CreateView):
	form_class = ParentForm
	model = Parent
	
	def form_valid(self, form):
		parent = form.save(commit=False)
		parent.created_by = self.request.user
		parent.save()
		return redirect('/waitlisty/')
		
	def get_success_url(self):
		return reverse('/waitlisty/')
	
	
@login_required
def index(request):
	parents= Parent.objects.filter(created_by=request.user)
	children = Child.objects.filter(created_by=request.user)
	
	return render(request, 'dashboard.html',
			{'parents':parents, 'children': children})
	
def disclaimer(request):
	return render(request, 'disclaimer.html')

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/waitlisty/')
		#Confirm Success
                state = "You're successfully logged in!"
            else:
		#Confirm Inactive
                state = "Your account is not active, please contact the site admin."
        else:
            #Confirm Fail
            state = "Your username and/or password were incorrect."

    return render(request, 'auth.html',{'state':state, 'username': username})

def profile(request):
    user_profile = request.user.get_profile()
    url = user_profile.url

    #OR
    url = request.user.get_profile().url
	
def logout_view(request):
    logout(request)
    return redirect(index)
    # Redirect to a success page.
