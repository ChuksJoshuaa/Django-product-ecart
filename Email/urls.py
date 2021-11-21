from django.urls import path

from . import views

urlpatterns = [
    path('email/', views.email_view, name='prod-email'),
]