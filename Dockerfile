    FROM python:3.12-alpine


    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    # Set work directory
    WORKDIR /var/www

    # Install system dependencies
    RUN apk update && apk add --no-cache \
        build-base \
        postgresql-dev

    # Install Python dependencies
    COPY requirements.txt .
    RUN pip install --upgrade pip
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy project
    COPY . .

    # Collect static files (optional, can be handled in docker-compose command)
    RUN python manage.py collectstatic --noinput

    # Make and apply migrations 
    RUN python3 manage.py makemigrations
    RUN python3 manage.py migrate

    # Switch to the non-root user
    # USER celeryuser
    # Create a non-root user
    USER celeryuser

    # Expose port 8000
    EXPOSE 8000

    # Default command (can be overridden in docker-compose.yml)
    CMD ["gunicorn", "BellzStudio.wsgi:application", "--bind", "0.0.0.0:8000"]

    # CMD ["celery", "-A", "your_app_name", "worker", "--uid=celeryuser"]
