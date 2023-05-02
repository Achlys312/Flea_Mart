# Use the official Python image as the base image.
FROM ubuntu:22.04

#upgrading and Installing pip 
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip 

# Copy the Django project files
COPY . .

# Install the dependencies.
RUN pip3 install -r requirements.txt

RUN pip3 install django-prometheus
# Expose port 8000 for the Django development server
EXPOSE 8000
# Configuring Prometheous
RUN apt-get update && apt-get install -y curl gnupg2 && \
    curl -s https://packages.grafana.com/gpg.key | apt-key add - && \
    echo "deb https://packages.grafana.com/oss/deb stable main" | tee /etc/apt/sources.list.d/grafana.list && \
    apt-get update && apt-get install -y grafana

# Run the Django development server
ENTRYPOINT python3 app/manage.py runserver 0.0.0.0:8000