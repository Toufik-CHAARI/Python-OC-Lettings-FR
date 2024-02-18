Database Structure and Data Models
==================================

This section outlines the database configuration and the structure of the data models used in the project. The project employs SQLite for development purposes due to its simplicity and ease of setup. The database schema includes two primary models: `Letting` and `Profile`.

Letting Model
-------------

The `Letting` model is designed to represent rental advertisements. Each letting has the following fields:

- **Name**: A descriptive title for the rental listing.
- **Address**: The physical address of the rental property.

This model allows the application to store and manage information about various rental listings available to users.

Profile Model
-------------

The `Profile` model represents the users of the application. It includes fields for:

- **Username**: The user's chosen username.
- **User**: A link to Django's default user model, facilitating access to built-in user functionalities like authentication and permissions.

By utilizing these models, the application effectively organizes and manages data related to rentals and users, facilitating efficient information retrieval and manipulation.

