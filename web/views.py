from django.shortcuts import render, HttpResponse, redirect
from web.models import enquiry
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']

        enq = enquiry(fname = fname, lname=lname, email=email, message=message)
        enq.save()
        messages.info(request, " Enquiry Submitted Successfully")
        return render(request, 'index.html')

    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pswd = request.POST.get('password')

        user = auth.authenticate(username = email, password = pswd)

        if user is not None:
            auth.login(request, user)
            request.session['uname'] = user.username
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


    return render(request, 'login.html')


def dashboard(request):
    if request.session.has_key('uname'):
        name = request.session['uname']
        enq = enquiry.objects.all()
        return render(request, 'dashboard.html',{'data': enq})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    print('User log out')
    return redirect('login')