Application Deployment and Management Procedures
================================================

Deployment of this Django application can be performed on cloud platforms such as Heroku or AWS.
The application uses Gunicorn as the WSGI server for serving the application and Whitenoise for serving static files.

**Setting Environment Variables**
---------------------------------

Ensure the necessary environment variables are set in CircleCi before deployment. These include:

- ``DOCKERHUB_PASS``: Your Docker Hub password.
- ``DOCKERHUB_USERNAME``: Your Docker Hub password username.
- ``HEROKU_API_KEY``: Your Heroku auth:Token.
- ``HEROKU_APP_NAME``: Your Heroku app name.

**Monitoring and Alerting**
---------------------------

It is crucial to set up a monitoring and alerting system for the application in production. Tools like Sentry are recommended for tracking and alerting on errors. This ensures that any issues can be promptly identified and resolved, maintaining the stability and reliability of the application.

By following these guidelines, you can deploy and manage your application effectively, ensuring a smooth operation in a production environment.

