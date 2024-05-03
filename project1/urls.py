from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import reverse_lazy

app_name = "project1"

urlpatterns = [
   path('', views.base, name='base'),
   path('register/', views.register, name='register'),
   path('logout/', views.logout_view, name='logout'),
   path('password-change/', views.PasswordResetView.as_view(), name='password_change_form'),
    path('password-change/done/', views.PasswordResetDoneView.as_view(), name='password_change_done'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset_view'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   #path('passwordreset/', views.password_reset_view, name='passwordreset'),
   #path('password_reset_view/', views.password_reset_view, name='password_reset_view'),
   #path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   #path('password-change/', PasswordChangeView.as_view(), name="password_change"),
#
   #path('password-change/done/', PasswordChangeDoneView.as_view(template_name="project1/password_change_done.html"), name="password_change_done"),
   #path('password-reset/',
   #      PasswordResetView.as_view(
   #         template_name="project1/password_reset_form.html",
   #         email_template_name="project1/password_reset_email.html",
   #         success_url=reverse_lazy("project1:password_reset_done")
   #      ),
   #      name='password_reset'),
   #path('password-reset/done/',
   #      PasswordResetDoneView.as_view(template_name="project1/password_reset_done.html"),
   #      name='password_reset_done'),
   #path('password-reset/<uidb64>/<token>/',
   #      PasswordResetConfirmView.as_view(
   #         template_name="project1/password_reset_confirm.html",
   #         success_url=reverse_lazy("project1:password_reset_complete")
   #      ),
   #      name='password_reset_confirm'),
   #path('password-reset/complete/',
   #      PasswordResetCompleteView.as_view(template_name="project1/password_reset_complete.html"),
   #      name='password_reset_complete'),
]
