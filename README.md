# To_Do_List

## About
This project implements a to do list with autentication. Its a simple application with back

## Frontend
- Node (React with Typescript)
    More type and controll.

### Start Frontend

## Backend
- Python (FastAPI)
    Better performance.

### Start Backend
uv run fastapi dev

## Database
- PostgreSQL
- SQLAlchemy
    Used for database queries.
- Alembic
    Used for more control and secure operation queries.

## Architecture
An simple monolith will take care of everything, the product is not scalable, it's a simple project.

todo-app/
│
├── frontend/                 # React + TypeScript
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   ├── contexts/
│   │   └── App.tsx
│   └── package.json
│
├── backend/                  # FastAPI
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── api/              # HTTP/API layer
│   │   │   ├── routes/
│   │   │   │   ├── auth.py
│   │   │   │   └── tasks.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── core/             # Configuration/security
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   │
│   │   ├── models/            # Database models
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   ├── schemas/           # Request/response schemas
│   │   │   ├── auth.py
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   ├── repositories/      # Database access
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   │
│   │   └── services/          # Business logic
│   │       ├── auth.py
│   │       └── task.py
│   │
│   ├── tests/
│   ├── alembic/
│   ├── requirements.txt
│   └── .env
│
├── docker-compose.yml
└── README.md