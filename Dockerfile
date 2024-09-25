# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Installing gunicord
RUN pip install gunicorn

# Copy the entire project into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port that your app runs on
EXPOSE 8000

# Command to run your application
CMD ["gunicorn", "AppQuiz.wsgi:application", "--bind", "0.0.0.0:8000"]
