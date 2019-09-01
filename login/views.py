from django.shortcuts import render,redirect
from .forms import Loginform
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        login_form = Loginform(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request,user)
            return redirect('show_st_info')
    else:
        login_form = Loginform()
    context = {}
    context['login_form'] = login_form
    return render(request,'login/login.html',context)

def login_out(request):
    logout(request)
    return redirect('user_login')