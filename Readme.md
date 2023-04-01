**Simple CRUD Based app on FASTapi**

This API allows you to add products.
The API is available at https://fastapi-fckw.onrender.com/

**ENDPOINTS**
______________________________________________________

First SignUp if you didn't register.

**SignUp**
-----------------------------------------------------

**POST** /user

SignUp page will open. Please signup if you didn't registered.

Every field is Required.

```
{
  "username": "dummy",
  "email": "dummmy@mygmail.com",
  "fullname": "dummy kumar",
  "disabled": True,
  "password" : "anything you want"
}
```


**GET** /user/{username}

Return the user details

NOTE- username is string type.


**LOGIN**
----------------------------------------------------

**POST** /login

Login before accessing the items. Get access token and its types after login.

```
{
  "username": "dummy",
  "password" : "what you had put while signup"
}
```

**ITEMS** - Requires Authentication
------------------------------------------------------

1. **GET** /item/

Get all the items inside the database


2. **GET** /item/{id}

Get details of item of given id.

NOTE- id is of type int.


3. **POST** /item/create

Allows you to submit a new item. 

The request body needs to be in JSON format and include the following properties:

name - String - Required

description - String - Required

price - float - Required

```
{
  "name": "Trouser",
  "description": "Cotton trouser",
  "price": 2000
}
```

4. **PUT** /item/{id}
Update the item by item id.

```
{
  "name": "Trouser",
  "description": "Gym trouser",
  "price": 2500
}
```

5. **DELETE** /item/{id}

Delete an existing item.

The request body needs to be empty.



