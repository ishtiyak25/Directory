
# Address Directory

Copy the whole project. <br>
Go to Project directory <i> cd Directory </i><br>
install all requirements:<br>
`` pip install -r requirements.txt``<br>
run the project:<br>
`` python manage.py runserver``<br>

### Admin Credentials
User: admin <br>
password: Abcd@1234

### Brows API urls

#### Country API
``http://127.0.0.1:8000/api/country`` <br>
Use this api url to fetch all country list. Use filter button to filter Country by name or Country code. <br>
###### Country Data
```angular2html
[
    {
        "Name": "Bangladesh",
        "Latitude": 20.86382,
        "Longitude": 88.15638,
        "Code": "BD"
    },
    {
        "Name": "Afghanistan",
        "Latitude": 335549.0,
        "Longitude": 674044.0,
        "Code": "AF"
    }
]
```
#### State API
``http://127.0.0.1:8000/api/state`` <br>
Use this api url to fetch all State list by country. Use filter button to filter State by name. <br>

###### State Data
```angular2html
[
    {
        "Country": "Bangladesh",
        "Name": "Dhaka"
    },
    {
        "Country": "Bangladesh",
        "Name": "Chottogram"
    },
    {
        "Country": "Bangladesh",
        "Name": "Rajshahi"
    }
]
```
#### Address API
``http://127.0.0.1:8000/api/address`` <br>
Use this api url to fetch address with state. User filter to filter address by house number and road number.
###### Address Data
```
[
    {
        "HouseNo": "15",
        "RoadNo": 15,
        "Name": "Nikunja-2, Khilkhet -1229",
        "State": "Dhaka"
    },
    {
        "HouseNo": "53",
        "RoadNo": 22,
        "Name": "Gulshan Avenue",
        "State": "Dhaka"
    }
]
```

#### Details address API
``http://127.0.0.1:8000/api/detail-address``
Use this API to fetch full address included state and country.
```angular2html
[
    {
        "HouseNo": "15",
        "RoadNo": 15,
        "Name": "Nikunja-2, Khilkhet -1229",
        "State": "Dhaka",
        "Country": "Bangladesh"
    },
    {
        "HouseNo": "53",
        "RoadNo": 22,
        "Name": "Gulshan Avenue",
        "State": "Dhaka",
        "Country": "Bangladesh"
    }
]
```

> I have used "rest_framework.authtoken" to authenticate API from external access. This project is currently providing authentication based on session. If anyone want to use above urls to fetch data he/she must have to be authenticated used.

> To test Application, run: python manage.py test