from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from wulfi.models import Profile, Banner

def login(request):
    profiles = Profile.objects.latest('updated') 
    banner = Banner.objects.latest('date_added')
    context = {
        'profiles': profiles,
        'banner': banner,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html', context)

def register(request):
    profiles = Profile.objects.latest('updated') 
    banner = Banner.objects.latest('date_added')

    context = {
        'profiles': profiles,
        'banner': banner,
    }

    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if username and email and password1 and password2:
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username taken...')
                    return render(request, 'register.html')

                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email taken...')
                    return render(request, 'register.html')

                else:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.save()
                    messages.info(request, 'User created')
                    return render(request, 'login.html')
            else:
                messages.info(request, 'Password did not match..')
            return render(request, 'register.html')

        else:
            messages.info(request, 'Fill all the fields')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
