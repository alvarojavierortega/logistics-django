# Logistics of package delivery

This Rest application helps to perform shipping logistics. It considers the following three models

- Client --> Defined by name, address, and phone number.
- Carrier --> Defined by name, vehicle type, and phone number.
- Package --> Defined by owner (related to Client's model), carrier (related to Carrier's model), size, weigh, origin address, destination address, and delivery status. 

## Used technologies

This project mainly uses the following technologies:

- Django
- Django Rest Framework

## How to run 

Please use the following command 

```python
docker compose up -d
```
or create a Python venv and install the requirements, and run the following commands

```python
python manage.py makemigrations logistics 
python manage.py migrate 
python manage.py initadmin
python manage.py runserver 0.0.0.0:8000
```

## How it works

### Endpoints descriptions

**Django-Admin**

- *http:localhost:8000/admin*    
    
    Please consider the following credentials:
    - user: admin
    - password: admin

**logistics application**

- *http:localhost:8000/api/package*

    You have access to CRUD operations over the package model. Furthermore, filtering options were added, such that you can list the registered packages and filter them by owner or carrier.

- *http:localhost:8000/api/carrier*

    GET: It displays a detailed list of the registered carriers. Filtering options are also available, i.e., filter by id or name. Because a carrier can have a large list of packages associated with, a query optimization was implemented to avoid problems in the future.

- *http:localhost:8000/api/client*

    GET: It displays a detailed list of the registered clients. Filtering options are also available, i.e., filter by id or name.
        
**dummy application**

- *http:localhost:8000/api/dummy/package/<<int:package_id>>/status/<<str:delivery_status>>*

    GET: It executes a dummy application that updates the delivery status of the specfied package. The delivery status variable has only some possible values that are: ["Shipped", "Delivered", "Canceled"]. 

- *http:localhost:8000/api/dummy/package/<int:package_id>/carrier/<str:carrier_id>*

    GET: It executes a dummy application that updates the carrier of the specfied package.

### How to register clients and carriers

The registration of clients and carriers is done through Django-admin page.

### How to register packages

The packages registration can be done either by Django-admin or POST request to *http:localhost:8000/api/package*.





