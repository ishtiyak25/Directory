from django.test import TestCase
from django.test import Client
# Create your tests here.
from django.conf import settings
from django.test import TestCase
from .models import *


class TestModels(TestCase):
    def test_model_str_country(self):
        data = Country.objects.count()
        self.assertEqual(data, 0)
        # success

    def test_get_client(self):
        data = {
            "Name": "Canada",
            "Code": " CN"
        }
        responseCountry = self.client.post("/api/country/", data=data)

        data = {
            "Name": "Dhaka",
        }
        responseState = self.client.post("/api/state/", data=data)

        self.assertEqual(responseCountry.status_code, 401)
        self.assertEqual(responseState.status_code, 401)
        # Failed type due to authentication

    def test_get_data_state(self):
        self.assertEqual(str(State.objects.count()), '0')
        # success but return 0 due to authentication

    def test_can_filter(self):
        Name = Country.objects.filter(Name='Bangladesh')
        Code = Country.objects.filter(Code='BD')
        self.assertEqual(Name.count(), 0)
        self.assertEqual(Code.count(), 0)
        # Failed

    def test_api_status(self):
        Cresponse = self.client.get('/api/country/')
        Sresponse = self.client.get('/api/state/')
        Aresponse = self.client.get('/api/address/')
        # Check that the response is 200 OK.
        self.assertEqual(Cresponse.status_code, 200)
        self.assertEqual(Sresponse.status_code, 200)
        self.assertEqual(Aresponse.status_code, 200)
        self.assertEqual(len(Cresponse.context['Name']), 2)
        self.assertEqual(len(Sresponse.context['Name']), 2)
        self.assertEqual(len(Aresponse.context['Name']), 2)



"""
Data is not testing or returning 0 due to authentication. Turn off authentication to get proper result
we can use more test case as CRUD.
Instead of testing every possible scenario i have tried to test on local and client and model.
"""
