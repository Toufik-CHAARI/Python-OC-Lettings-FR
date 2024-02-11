# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Creating a virtual environment and using it
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Upgrade pip and install any needed packages specified in requirements.txt
# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install --no-cache-dir --max-concurrent-downloads 10 -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define command to run the application using Gunicorn, bind to PORT with a default of 8000 if not specified
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
