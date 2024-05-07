from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
from user.forms import CreateUserForm
from user.forms import UserUpdateForm,ProfileUpdate
from django.contrib.auth import logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}. Continue to Login')
            return redirect('user-login')
            
    else:
        form=CreateUserForm()
        
            
    context={
        'form':form
    }
    return render(request,'user/register.html',context)

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request,data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             print(user)
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         initial_data = {'username': '', 'password': ''}
#         form = UserCreationForm(initial=initial_data)
#     return render(request, 'user/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request,'user/logout.html')

@login_required
def profile(request):
    return render(request,'user/profile.html')

@login_required
def profile_update(request):
    if request.method=='POST':
        user_form= UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
            
    else:
        user_form= UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdate(instance=request.user.profile)  
    context={
        'user_form':UserUpdateForm,
        'profile_form':ProfileUpdate
    }
    return render(request,'user/profile_update.html',context)





