from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm

# Create your views here.s

User = get_user_model()

# views for listing all users (e.g., students or instructors)
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

# views for displaying a specific user's details
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_detail.html', {'user': user})

# view for creating a new user

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user_list')  # Redirect after successful creation
    else:
        form = CustomUserCreationForm()  # if GET request, show empty form
    return render(request, 'accounts/create_user.html', {'form': form})