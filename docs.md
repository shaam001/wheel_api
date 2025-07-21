# Tech stack used
- python 3.12
- Django (with Gunicorn for production server)
- Django REST Framework
- PostgreSQL (as the database)
- Docker

# Download or clone the github repository
- https://github.com/shaam001/wheel_api

# implemented APIs
- Wheel Specifications API (GET and POST)
- Bogie Checksheet API

# Running the project without Docker
- Running the project without Docker may lead to issues if PostgreSQL is not properly configured on the system.
## If you still prefer to run it without Docker:
- Either configure PostgreSQL with the required credentials manually, OR
- Remove the database-related settings from settings.py and use sqlite3 for quick local testing.

## Using Docker is recommended 


# Running the Project with Docker
- Running without docker 
- Make sure you have the following installed on your system:
### Docker
### Docker Compose

#  Build the Docker Image
## for windows docker build run
- docker build -t wheel_api .

## For Linux/macOS:
- sudo docker build -t wheel_api .

# start the container app
- docker-compose up --build

# your app should be running at
- http://127.0.0.1:8000/

# Test the api using postman
- collection link: 
- Ensure local server is running at http://localhost:8000.
- Run the API requests from the collection.