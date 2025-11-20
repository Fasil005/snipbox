# SnipBox

A Django REST Framework application for managing code snippets with tags and user associations.

## Project Setup

### Clone the project:

```bash
git clone https://github.com/Fasil005/snipbox.git
cd SnipBox
```

## Environment Configuration

### Copy the sample environment file:

```bash
cp .env.sample .env
```


Open .env and update all variable values to match your environment (database name, passwords, secret key, etc.).

## Docker Build and Run

### Build and Start Services

Build the Docker images and start all services (database and Django application):

```bash
docker compose up --build
```

## Database Migrations

### Initial Setup

After starting the containers, run migrations:

```bash
docker compose exec django python manage.py migrate
```
**This migration creates a test user that can be used to log in, obtain access tokens, and test all APIs.**

### Create Superuser

To create a Django admin superuser:

```bash
docker compose exec django python manage.py createsuperuser
```

Follow the prompts to enter username, email, and password.


## Usage

### Access the Application

- **Django Application**: http://localhost:8088
- **Django Admin**: http://localhost:8088/admin
