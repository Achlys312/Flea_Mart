# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Django project files
COPY . /app

# Set the working directory to /app
#WORKDIR /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django development server
CMD ["pipenv", "run","python", "manage.py", "runserver", "0.0.0.0:8000"]