# API Authentication

## Overview
This API uses token-based authentication to secure endpoints. Only authenticated users can access the inventory endpoints.

### Authentication Steps:
1. Obtain a token using the `/api-token-auth/` endpoint.
   - **Request**:
     ```
     POST /api-token-auth/
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```
   - **Response**:
     ```
     {
         "token": "your_token"
     }
     ```

2. Include the token in the `Authorization` header for subsequent API requests:
   - **Header**:
     ```
     Authorization: Token your_token
     ```

### Endpoints Requiring Authentication:
- **GET /api/inventory/**: Retrieve the list of inventory items.
- **POST /api/inventory/**: Create a new inventory item.

### Testing:
Use Postman, curl, or automated test scripts to verify the authentication setup.
