from django.conf.urls import url
from authentication.views import RegistrationView,UserLoginView

urlpatterns = [
    url(r'^signup',RegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),

]
