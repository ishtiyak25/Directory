from django.urls import path

from addressBook.views import CountryList, StateList

urlpatterns = [
    path("api/country", CountryList.as_view(), name="country"),
    path("api/state", StateList.as_view(), name="state"),
]