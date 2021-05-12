# authy-API

API to perform the following calls to the specified roles.

*(Without authentication)*

## Role-Admin :
1. **API: Add an advisor**
    1. **Method:** POST
    2. **Endpoint:** /admin/advisor/
    3. **Request:**
        1. Advisor name
        2. Advisor Photo URL
    4. **Response:** No Response
    5. **Status:**
        - 200_OK if the request is successful
        - 400_BAD_REQUEST if any of the request fields are missing
## Role-User :
1. **API: Can register as a user**
    1. **Method:** POST
    2. **Endpoint:** /user/register/
    3. **Request:**
        1. Name
        2. Email
        3. Password
    4. **Response:**
        1. JWT Authentication Token
        2. User id
    5. **Status:**
        - 200_OK if the request is successful
        - 400_BAD_REQUEST if any of the request fields are missing
2. **API: Can log in as a user**
    1. **Method:** POST
    2. **Endpoint:** /user/login/
    3. **Request:**
        1. Email
        2. Password
    4. **Response:**
        1. JWT Authentication Token
        2. User id
    5. **Status:**
        - 200_OK if the request is successful
        - 400_BAD_REQUEST if any of the request fields are missing
        - 401_AUTHENTICATION_ERROR if the email/password combination was wrong
3. **API: Get the list of advisors**
    1. **Method:** GET
    2. **Endpoint:** /user/\<user-id\>/advisor/
    3. **Request:** None
    4. **Response:**
        - An array of advisor objects with each object having:
            1. Advisor Name
            2. Advisor Profile Pic
            3. Advisor Id
    5. **Status:**
        - 200_OK if the request is successful
4. **API: Can book call with an advisor**
    1. **Method:** POST
    2. **Endpoint:** /user/\<user-id\>/advisor/\<advisor-id\>/
    3. **Request:**
        1. Booking time (a DateTime string) *eg: "2016-12-05T12:34:56.000000Z"*
    4. **Response:** None
    5. **Status:**
        - 200_OK if the request is successful
5. **API: Can get all the booked calls**
    1. **Method:** GET
    2. **Endpoint:** /user/\<user-id\>/advisor/booking/
    3. **Request:** None
    4. **Response:**
        - An array of advisor objects with each object having
            1. Advisor Name
            2. Advisor Profile Pic
            3. Advisor Id
            4. Booking time
            5. Booking id
    5. **Status:**
        - 200_OK if the request is successful