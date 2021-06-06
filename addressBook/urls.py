from django.urls import path

from addressBook.views import CountryList, StateList, AddressList, DetailAddressList

urlpatterns = [
    path("api/country", CountryList.as_view(), name="country"),
    path("api/state", StateList.as_view(), name="state"),
    path("api/address", AddressList.as_view(), name="address"),
    path("api/detail-address", DetailAddressList.as_view(), name="details_address"),
]