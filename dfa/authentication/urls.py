from django.urls import path

from .views import LoginAPIView, UserRetrieveUpdateAPIView, RegistrationAPIView

app_name = 'authentication'
urlpatterns = [
    path('me/', UserRetrieveUpdateAPIView.as_view()),
    path('signup/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
