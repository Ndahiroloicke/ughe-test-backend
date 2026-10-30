# UGHE Test Web App — Backend (Django)

Django REST API and Django Admin for the UGHE homepage assessment. Pairs with the [Next.js frontend](https://github.com/ndahiroloicke/ughe-test-frontend).

**This repository:** https://github.com/ndahiroloicke/ughe-test-backend  
**Frontend repository:** https://github.com/ndahiroloicke/ughe-test-frontend

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)

## Run with Docker (recommended)

Clone this repo, then from the **repository root** (where `docker-compose.yml` and `Dockerfile` live):

```bash
docker compose up --build
```

On first start the container will:

1. Run PostgreSQL migrations  
2. Seed UGHE homepage content (`seed_ughe`) if the database is empty  
3. Start Gunicorn on port **8000**

### URLs

| Service | URL |
|---------|-----|
| Homepage API (JSON) | http://localhost:8000/api/homepage/ |
| Django Admin | http://localhost:8000/admin/ |
| Login API | http://localhost:8000/api/auth/login/ |

### Credentials

| Purpose | Username | Password |
|---------|----------|----------|
| Admin + app login | `ughe_admin` | `UGHE_Test_2024!` |

Stop containers:

```bash
docker compose down
```

To reset the database volume:

```bash
docker compose down -v
docker compose up --build
```

## Run locally without Docker (optional)

Requires Python 3.12+ and a PostgreSQL instance.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

set POSTGRES_DB=ughe_db
set POSTGRES_USER=ughe_user
set POSTGRES_PASSWORD=ughe_pass
set POSTGRES_HOST=localhost
set POSTGRES_PORT=5432
set CORS_ALLOWED_ORIGINS=http://localhost:3000

python manage.py migrate
python manage.py seed_ughe
python manage.py runserver
```

## Connect the frontend

Start **this backend first** on port **8000**, then run the frontend repo (see its README). The frontend expects:

- Browser: `NEXT_PUBLIC_API_URL=http://localhost:8000/api`
- CORS is already allowed for `http://localhost:3000` in Docker settings.

## REST API

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/homepage/` | All homepage content for Next.js |
| POST | `/api/auth/login/` | JSON body: `{"username","password"}` → JWT |
| GET | `/api/auth/me/` | Header: `Authorization: Bearer <access>` |
| POST | `/api/auth/refresh/` | Refresh token (Simple JWT) |

## Django Admin content models

- Site branding, utility nav links, main nav items  
- Hero slides (image or video URL)  
- Facts & Stats section and stat blocks  

## Dependencies

See `requirements.txt`. Main libraries: Django, djangorestframework, djangorestframework-simplejwt, psycopg2-binary, django-cors-headers, gunicorn.

## More documentation

See `readme.txt` in this repo for the full assessment write-up and evaluation checklist.
