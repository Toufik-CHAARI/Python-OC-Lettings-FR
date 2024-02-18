Project Installation Instructions
=================================

To install the project, follow these steps:

1. Clone the GitHub repository.

2. Set up a virtual environment with ``python3.10 -m venv venv``.

3. Activate the virtual environment:

   - On Unix, use: ``source venv/bin/activate``.
   - On Windows, use: ``venv\Scripts\activate``.

4. Install the dependencies with ``pip install -r requirements.txt``.

5. Apply the migrations with ``python manage.py migrate``.

6. Start the development server with ``python manage.py runserver``.

7. The admin interface can be accessed with username: ``admin`` and password: ``Abc1234!``.

