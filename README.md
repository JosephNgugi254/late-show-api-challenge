# Late Show API Challenge

A Flask REST API for managing a Late Night TV show system, built with PostgreSQL, JWT authentication, and tested with Postman.

## Clone the Repository

```bash
git clone https://github.com/JosephNgugi254/late-show-api-challenge.git
cd late-show-api-challenge
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 16
- Pipenv
- Postman

### Installation

Install dependencies:

```bash
pipenv install
pipenv shell
```

Set up PostgreSQL:

```sql
psql -U postgres -h localhost
CREATE DATABASE late_show_db;
\q
```

Create a `.env` file in the project root:

```env
DATABASE_URI=postgresql://postgres:<your-password>@localhost:5432/late_show_db
JWT_SECRET_KEY=super-secret-123
```

Run migrations and seed the database:

```bash
export FLASK_APP=server.app
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

## Run the Application

```bash
python server/app.py
```

API available at [http://localhost:5000](http://localhost:5000).

Test endpoints with Postman.

---

## API Endpoints

| Route                | Method | Auth Required | Description                          |
|----------------------|--------|---------------|--------------------------------------|
| `/register`          | POST   | No            | Register a new user                  |
| `/login`             | POST   | No            | Get JWT token                        |
| `/episodes`          | GET    | No            | List all episodes                    |
| `/episodes/<id>`     | GET    | No            | Get episode details with appearances |
| `/episodes/<id>`     | DELETE | Yes           | Delete episode and appearances       |
| `/guests`            | GET    | No            | List all guests                      |
| `/appearances`       | POST   | Yes           | Create a new appearance              |

---

## Example Requests

**POST /register**

```json
{
   "username": "testuser",
   "password": "testpass"
}
```

**POST /login** (save token for auth)

```json
{
   "username": "testuser",
   "password": "testpass"
}
```

**POST /appearances** (use `Authorization: Bearer <token>`)

```json
{
   "rating": 3,
   "guest_id": 1,
   "episode_id": 1
}
```

---

## Postman Testing

- Import `challenge-4-lateshow.postman_collection.json` (if provided).
- Test endpoints, using JWT token for protected routes (`DELETE /episodes/<id>`, `POST /appearances`).
