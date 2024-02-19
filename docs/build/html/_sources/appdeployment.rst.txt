Application Deployment and Management Procedures
================================================

Deployment of this Django application can be performed on cloud platforms such as Heroku or AWS. The application uses Gunicorn as the WSGI server for serving the application and Whitenoise for serving static files. A CI/CD pipeline has been implemented via CircleCi, and containerization is performed via Docker Hub & Docker Desktop. The pipeline is composed of three steps:

1. Testing and Linting
2. Build and push Docker Image
3. Deployment to Heroku

Please note that any change applied to a given branch triggers only the first job (testing & linting). The full workflow from testing to deployment is only triggered by changes applied to the master branch, providing that no error has been raised.

Requirements
------------

- **Create an Heroku app:** Initialize an application on Heroku.
- **Build a Docker image of the project locally:** Use Docker Desktop to build your application's Docker image.
- **Push the Docker image to Docker Hub:** Upload your Docker image to your Docker Hub repository.
- **Create a CircleCI project:** Set up your project on CircleCI for continuous integration.
- **Create a Sentry account and update the DSN key in settings.py:** Sign up for Sentry and configure it to monitor your application.

Setting Environment Variables
-----------------------------

Ensure the necessary environment variables are set in CircleCi before deployment. These include:

- **SSH Keys:** set up your public key in your CircleCi and GitHub project.
- **DOCKERHUB_USERNAME:** Your Docker Hub username.
- **DOCKERHUB_PASS:** Your Docker Hub password.
- **HEROKU_API_KEY:** Your Heroku auth token.
- **HEROKU_APP_NAME:** Your Heroku app name.

Monitoring and Alerting
-----------------------

Setting up a monitoring and alerting system for applications in production is crucial. Implement tools like Sentry for tracking and alerting on errors. This ensures that any issues can be promptly identified and resolved, maintaining the stability and reliability of the application.

Run the Latest Image of the App Locally
---------------------------------------

To run the latest image of the application locally:

- Navigate to the root project directory.
- Activate the virtual environment.
- Execute the following commands:

  .. code-block:: bash

      export DOCKERHUB_USERNAME=your_docker_username
      chmod +x run_docker.sh
      ./run_docker.sh

Follow these guidelines to deploy and manage your application effectively, ensuring smooth operation in a production environment.
