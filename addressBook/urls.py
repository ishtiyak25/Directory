from django.urls import path

from addressBook.views import CountryList

urlpatterns = [
    path("api/country", CountryList.as_view(), name="country")
]