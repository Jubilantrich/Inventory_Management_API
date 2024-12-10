# Inventory_Management_API
alx capstone project

# Inventory_Management_API
alx capstone project

1. Project Title and Description
Title: Inventory Management API
Description:
This project involves developing a RESTful API to manage a store's inventory. The API will allow authorized users to perform CRUD operations for inventory items and users. Additionally, it will provide an endpoint to view real-time inventory levels. The API will utilize Django ORM for database interactions and will be deployed on PythonAnywhere for accessibility.

2. Core Features and Functionality
Inventory Management:
Add new inventory items.
Update existing inventory details.
Delete inventory items.
View inventory levels, including item name, quantity, and availability.
User Management:
Create new users with roles (e.g., Admin, Manager, SalesPerson).
Update user information.
Delete users.
Authenticate users with token-based authentication (using Django REST Framework).
Security:
Role-based access control to restrict certain API operations (e.g., only admins can delete inventory items).
Secure communication using HTTPS.
Deployment:
Host the API on a cloud platform (PythonAnywhere).
3. API Endpoints to Implement
User Management Endpoints:
POST /users/ - Create a new user.
PUT /users/<id>/ - Update user details.
DELETE /users/<id>/ - Delete a user.
POST /auth/login/ - Authenticate a user and return a token.
Inventory Management Endpoints:
POST /inventory/ - Add a new inventory item.
GET /inventory/ - View all inventory items.
GET /inventory/<id>/ - Retrieve details of a specific inventory item.
PUT /inventory/<id>/ - Update details of a specific inventory item.
DELETE /inventory/<id>/ - Delete an inventory item.
Inventory Levels:
GET /inventory/levels/ - Retrieve real-time inventory levels.

4. Tools and Libraries to Use
Development Tools:
Python 3.x
Django 4.x
Django REST Framework (DRF)
Database and ORM:
MySQL Database
Django ORM
Authentication:
Django REST Framework Token Authentication
Deployment:
PythonAnywhere
Version Control:
Git (with GitHub for repository hosting)
Documentation:
DRF's built-in API documentation
Testing:
Django Test Framework (for unit tests)

Data Model Design


User:
Contains details about users such as id, username, password, and role.
Each user can manage multiple inventory items.
Inventory:
Contains details of inventory items such as id, name, quantity,price and a foreign key user_id linking it to the user responsible for managing it.
Each inventory item is linked to one user (owner/manager).
Relationship:
1-to-Many: A single User can manage multiple Inventory items, but each Inventory item is owned by only one User.


