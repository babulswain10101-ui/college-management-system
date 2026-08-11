from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .forms import LoginForm, RegisterForm


# =========================================================
# LOGIN
# =========================================================

def login_view(request):

    # Already logged in
    if request.user.is_authenticated:
        return redirect("dashboard")

    # Login form
    form = LoginForm(
        request,
        data=request.POST or None
    )

    # POST request
    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                # Protected page se login par aaya ho
                next_url = request.GET.get("next")

                if next_url:
                    return redirect(next_url)

                # Admin
                if user.is_superuser:
                    return redirect("dashboard")

                # Teacher
                elif hasattr(user, "teacher"):
                    return redirect("teachers")

                # Student
                elif hasattr(user, "student"):
                    return redirect("students")

                # Normal user
                else:
                    return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    # IMPORTANT:
    # GET + invalid POST dono me login page return hoga
    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )

# =========================================================
# LOGOUT
# =========================================================

def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully."
    )

    return redirect("login")


# =========================================================
# REGISTER
# =========================================================

def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Form se User object create karo
            user = form.save(commit=False)

            # Password ko securely hash karo
            user.set_password(
                form.cleaned_data["password"]
            )

            # First Name
            user.first_name = form.cleaned_data[
                "first_name"
            ]

            # Last Name
            user.last_name = form.cleaned_data[
                "last_name"
            ]

            # Username aur email form se automatically
            # aa jayenge

            user.save()

            messages.success(
                request,
                "Account created successfully. Please login."
            )

            return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


# =========================================================
# CHANGE PASSWORD
# =========================================================

@login_required
def change_password_view(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            # Password change ke baad
            # user logout nahi hoga
            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Password changed successfully."
            )

            return redirect("profile")

    else:

        form = PasswordChangeForm(
            request.user
        )

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form
        }
    )


# =========================================================
# FORGOT PASSWORD
# =========================================================

def forgot_password_view(request):

    return render(
        request,
        "accounts/forgot_password.html"
    )


# =========================================================
# PROFILE
# =========================================================

@login_required
def profile_view(request):

    user = request.user

    # First Name + Last Name ko ek saath karo
    full_name = f"{user.first_name} {user.last_name}".strip()

    # Agar name nahi hai
    if not full_name:
        full_name = "Not provided"

    return render(
        request,
        "accounts/profile.html",
        {
            "user": user,
            "full_name": full_name,
        }
    )

