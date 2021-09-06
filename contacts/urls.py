from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('enquiry/', views.enquiry, name='enquiry'),
]
