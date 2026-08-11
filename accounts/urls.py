from django.urls import path
from . import views


urlpatterns = [

    # Login
    path(
        "login/",
        views.login_view,
        name="login"
    ),

    # Logout
    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    # Register
    path(
        "register/",
        views.register_view,
        name="register"
    ),

    # Change Password
    path(
        "change-password/",
        views.change_password_view,
        name="change_password"
    ),

    # Forgot Password
    path(
        "forgot-password/",
        views.forgot_password_view,
        name="forgot_password"
    ),

    # Profile
    path(
        "profile/",
        views.profile_view,
        name="profile"
    ),

]