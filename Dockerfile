# Use the official Python image as the base image
FROM ubuntu:22.04

#upgrading and Installing pip 
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip

# Copy the Django project files
COPY . .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django development server
ENTRYPOINT python3 app/manage.py runserver 0.0.0.0:8000