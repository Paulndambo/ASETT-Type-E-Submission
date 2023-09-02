from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage

from django.contrib.auth.models import User
from cryptoapp.models import Wallet

# Create your views here.

def register(request, referral_code = None):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")

        user_by_email = User.objects.filter(email=email).first()
        user_by_username = User.objects.filter(username=username).first()


        if user_by_email:
            messages.error(request, f"User with this email exists already, try a different email!!")

        elif user_by_username:
            messages.error(request, f"User with this username exists already, try a different username!!")

            print(username, email, first_name, last_name, password)
        else:
            user = User.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()

            wallet = Wallet.objects.create(
                user=user,
                phone_number=phone_number
            )
            ref_code = f"{user.id}{wallet.id}" * 2
            wallet.referral_code = str(ref_code)
            wallet.save()
            if referral_code:
                inviting_wallet = Wallet.objects.filter(referral_code=referral_code).first()
                inviting_user = User.objects.filter(id=inviting_wallet.user.id).first()
                wallet.invited_by = inviting_user
                wallet.save()
            messages.success(request, f"User created successfully!!")

            return redirect('login')
    
    context = {
        "referral_code": referral_code
    }
    
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def invite_new_user(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        referral_link = request.POST.get("referral_link")
        print(f"Invited User Email: {email}")
        html_message = render(request, 'accounts/invite_email.html', {'referral_link': referral_link}).content.decode('utf-8')

        mail = EmailMessage(
            "Welcome to Crypto App",
            html_message,
            "cryptoappdjango@gmail.com",
            [email,]
        )
        mail.content_subtype = "html"
        mail.send(fail_silently=False)
        return redirect("wallet")
    return render(request, "modals/invite_user.html")