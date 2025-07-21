# Tech stack used
- python 3.12
- Django (with Gunicorn for production server)
- PostgreSQL (as the database)
- Docker

# Running the Project with Docker
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