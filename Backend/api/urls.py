from django.urls import path #uses for path making
from .views import echo  # Check if it is 'echo' or 'echo_view'
#opening path for ux call
#this is the path for api which is added by main file
urlpatterns = [
    path("echo/", echo), # No 'api/' here, it's added by the main file
]

