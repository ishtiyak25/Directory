from django.db import models


# ************************************* Country Info ****************************************************
class Country(models.Model):
    Name = models.CharField(blank=False, max_length=90, verbose_name="Country")
    Latitude = models.FloatField(null=False, verbose_name="Latitude")
    Longitude = models.FloatField(null=False, verbose_name="Longitude")
    Code = models.CharField(blank=False, max_length=4, verbose_name="Code")
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.Name)

    class Meta:
        managed = True
        db_table = "Country"


# *************************** Country respected state info **********************************
class State(models.Model):
    Name = models.CharField(blank=False, max_length=90, verbose_name="State")
    # foreign Key
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.Name)

    class Meta:
        managed = True
        db_table = "State"


# *************************** Country, State respected Address **********************************
class Address(models.Model):
    Name = models.CharField(blank=False, max_length=255, verbose_name="Address")
    HouseNo = models.CharField(blank=False, max_length=90, verbose_name="House No")
    RoadNo = models.IntegerField(verbose_name="Road No")
    # foreign Key
    State = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="State")
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country")

    def __str__(self):
        return "{}".format(self.Name)

    class Meta:
        managed = True
        db_table = "Address"
