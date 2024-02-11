# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Install any needed packages specified in requirements.txt
# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /code/
# Upgrade pip
RUN pip install --upgrade pip
# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



# Copy the current directory contents into the container at /code
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define command to run the application
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
#CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:${PORT:-8000}
