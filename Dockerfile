FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    python manage.py createsuperuser --noinput || true && \
    gunicorn --bind 0.0.0.0:8000 \
    wheel_api.wsgi:application"]