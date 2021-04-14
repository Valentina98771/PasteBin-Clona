from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pastes/', include('pastes.urls')),
    path('user/', include('user.urls')),
    path('pastes/', include('django.contrib.auth.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='detail.html'), name='detail'),
    path('pastes/', include('social_django.urls', namespace='social')), 
    path('user/', include('social_django.urls', namespace='social')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 
]
