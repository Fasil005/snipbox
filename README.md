# SnipBox

A Django REST Framework application for managing code snippets with tags and user associations.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (version 20.10 or later)
- **Docker Compose** (version 2.0 or later)


## Docker Installation

Install Docker Desktop by following the official Docker documentation:

👉 **Official Docker Install Guide:**  
https://docs.docker.com/get-docker/

Verify installation:

```bash
docker --version
docker compose version
```

## Project Setup

### Clone the project:

```bash
git clone <repository-url>
cd SnipBox
```

## Environment Configuration

### Copy the sample environment file:

```bash
cp .env.sample .env
```


Open .env and update all variable values to match your environment (database name, passwords, secret key, etc.).

⚠️ Do NOT use .env.sample values directly in production. Update them with your secure values.

## Docker Build and Run

### Build and Start Services

Build the Docker images and start all services (database and Django application):

```bash
docker compose up --build
```

This command will:
- Build the Django application image
- Pull the PostgreSQL image
- Start both containers
- Set up volumes for persistent data

### Run in Detached Mode

To run containers in the background:

```bash
docker compose up -d --build
```

### View Running Containers

```bash
docker compose ps
```

### View Logs

View logs from all services:
```bash
docker compose logs
```

View logs from a specific service:
```bash
docker compose logs django
docker compose logs db
```

Follow logs in real-time:
```bash
docker compose logs -f django
```

### Stop Services

Stop all running containers:
```bash
docker compose down
```

### Rebuild After Changes

If you make changes to the code or dependencies:

```bash
docker compose up --build
```

Or rebuild specific service:
```bash
docker compose build django
docker compose up -d
```

## Database Migrations

### Initial Setup

After starting the containers, run migrations:

```bash
# Execute migrations inside the Django container
docker compose exec django python manage.py migrate
```

### Create New Migrations

If you modify models:

```bash
# Create migration files
docker compose exec django python manage.py makemigrations

# Apply migrations
docker compose exec django python manage.py migrate
```

### Create Superuser

To create a Django admin superuser:

```bash
docker compose exec django python manage.py createsuperuser
```

Follow the prompts to enter username, email, and password.

### Access Django Shell

```bash
docker compose exec django python manage.py shell
```

### Reset Database (Development Only)

⚠️ **WARNING**: This will delete all data!

```bash
# Stop containers and remove volumes
docker compose down -v

# Start containers again
docker compose up -d

# Run migrations
docker compose exec django python manage.py migrate

# Create superuser
docker compose exec django python manage.py createsuperuser
```

## Usage

### Access the Application

- **Django Application**: http://localhost:8088
- **Django Admin**: http://localhost:8088/admin


## Development

### Running Commands Inside Containers

Execute any Django management command:

```bash
docker compose exec django python manage.py <command>
```

Examples:
```bash
# Collect static files
docker compose exec django python manage.py collectstatic

# Show migration status
docker compose exec django python manage.py showmigrations
```

### Accessing Database Directly

```bash
# Connect to PostgreSQL using psql
docker compose exec db psql -U <db_username> -d <db_name>
```


### Port Already in Use

#### Port Configuration

The project uses ports from the `.env` file so you can change them easily without editing Docker files.



If port 8088 or 5433 is already in use, modify the ports in `.env`:

```bash
DJANGO_PORT=8088
DJANGO_EXPOSED_PORT=8088

DB_PORT=5432
DB_EXPOSED_PORT=5432
```
**NB:** If you change any values in the `.env` file (including ports), you must rebuild the containers

## Support

For issues or questions, please open an issue in the repository.

---

**Happy Coding! 🚀**
