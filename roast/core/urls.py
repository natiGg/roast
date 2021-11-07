from django.conf.urls import url
from core.views import RegistrationView

urlpatterns = [
    url(r'^signup',RegistrationView.as_view())
]
