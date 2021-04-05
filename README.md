# Library App

## Introduction
A REST-based library client using open-library API tested with Python 3.9. 
 
Our application uses external API from [open-library.org]() for developers which don’t need key or any authentication. We have a simple user interface for our application so the information about books and users can be shown.  

Our app is developed in Python and Django framework.
REST-based service interface for CRUD
use sql_server.pyodbc to connect to the Azure database
Interaction with external API from open library
Use Microsoft Azure cloud database for persisting information.

The password of user account is encrpyted by hash and the Azure database is secured with role-based policies.

Our app is not serving in over https so you can run it on [http://127.0.0.1:8000]()

Group 35 members: Felix Xavier Saiz,Muhammad Hassan Rasheed, Oliver Whiteley, Akshay Singh Rajput, Zihang Pan




## Installation
- Our app is not serving on https. So you have to download it and install.
- First you need to install python 3.9 in your machine and you can use pip to install the other packages.
- You also need to install Django framework to run the app.
	`$ pip install Django==3.0.10`
	
- Here are some other packages needed.


	```
	$ pip install pandas
	$ pip install djangorestframework
	$ pip install django-crispy-forms
	$ pip install django-mssql-backend
	$ pip install Pillow
	```
- You should also install olclient.openlibrary module from [https://github.com/internetarchive/openlibrary-client
](https://github.com/internetarchive/openlibrary-client)

	or clone the project from 
	`git clone https://github.com/internetarchive/openlibrary-client`
- You should download ODBC driver for SQL server from
	- [https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server?view=sql-server-ver15) (Windows)

	- [https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15) (MacOS)

- To install our app 

	`$ git clone https://github.com/mhassanrasheed/library.git ` 
	and switch to felix_branch.
	
	Or you can go to 
	 [https://github.com/mhassanrasheed/library/tree/felix_branch](https://github.com/mhassanrasheed/library/tree/felix_branch)
	 and download the zip file.
	
## Configuration	
Database connection is already set in the settings.py in Django
## Usage
- In this library app, admin user can create resources, subjects, authors, locations,  get informations from , search for a book with different criteria (subjects, authors, locations, resources)loan, delete loan and.
- To request the APIs
	- 'admin/'
	- 'upload/'
	- 'update/<<int:resource_id>>'
	- 'delete/<<int:resource_id>>'
	-  'home/'
    - 'register/'
    - 'profile/'
	- 'resource_api/' 
    - 'resource-list/'    
    - 'resource-detail/<<str:pk>>/'    
    - 'resource-create/'   
    - 'resource-update/<<str:pk>>/'    
    - 'location-list/'
    - 'location-detail/<<str:pk>>/'
    - 'location-create/'
    - 'location-update/<<str:pk>>/'
    - 'subject-list/'
    - 'subject-detail/<<str:pk>>/'
    - 'subject-create/'
    - 'subject-update/<<str:pk>>/'
   
   
    
### For admin user 


- First, you need to register an admin account  from 
- Admin user can add new books, edit information of books and delete books. Admin user can also create and delete subjects, authors, locations, resources. The 
- Admin users can also check the resources about the books and user profiles such as user loans and user list. Only admin users can change the information of users and books according to role-based policies.


### For readers 


- Register
	- Readers can create their accounts using username, E-mail and password(hash-based authentication) to join our library.
- Creating loans and return
	- Readers can be given loans of the book or return books once they log in. 
- Profile 
	- Readers can check their own profiles. They can see what they have loaned.
