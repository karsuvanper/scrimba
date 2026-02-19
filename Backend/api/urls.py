from django.urls import path
from .views import echo  # Check if it is 'echo' or 'echo_view'
#opening path for ux call
urlpatterns = [
    path("echo/", echo), # No 'api/' here, it's added by the main file
]

