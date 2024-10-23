# Cookie Stand API 

Cookie Stand application using CodeFellows template for Django CRUD API, plus Postgres17 + Docker

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/cookie-stand-api.git
cd cookie-stand-api
```

### Environment Variables
Create a .env file in the root directory based on .env.sample. The file should include:


```
SECRET_KEY=your_secret_key
DB_NAME=cookie_stand_db
DB_USER=cookie_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Install Dependencies

`pip install -r requirements.txt`

### Run Migrations

`python manage.py makemigrations`
`python manage.py migrate`

### Create Superuser

To create an admin user, run:


`python manage.py createsuperuser`

### Running the Project

**Docker Setup**

The project uses Docker for development. Ensure Docker is installed on your machine.

*Build and Run Containers*

`docker compose up --build`

*Stop Containers*

`docker compose down`

*Restart Containers*

`docker compose restart`

*Collect Static Files*

`docker compose run web python manage.py collectstatic`

*Migrate the Database*

`docker compose run web python manage.py migrate`

### Testing

**Running Unit Tests**

Unit tests are located in cookie_stands/tests.py. To run the tests, use:

`docker compose run web python manage.py test`

**Manual API Testing**

Manually confirm the API endpoints using API Tester, Postman, or HTTPie. Example HTTPie commands:

*List Cookie Stands:*


http GET http://localhost:8000/api/cookie_stands/

*Create a New Cookie Stand:*

http POST http://localhost:8000/api/cookie_stands/ location="New Stand" description="Fresh cookies daily" minimum_customers_per_hour=10 maximum_customers_per_hour=50 average_cookies_per_sale=2.5

*Project Structure*

`cookie_stands/`: Contains the CookieStand model, views, serializers, and tests.

`templates/cookie_stands/:` HTML templates for the CookieStand views.

`docker-compose.yml`: Docker Compose setup for the project.

`.env:` Environment variables file.

