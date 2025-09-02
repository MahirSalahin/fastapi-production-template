# 🚀 FastAPI Template

A production-ready FastAPI template with a clean, scalable architecture following best practices and conventions.

## 🔧 Tech Stack
**FastAPI + SQLModel + Alembic + Pydantic Settings**


## 📋 Requirements

- Python 3.8+
- PostgreSQL

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   FRONTEND_URL=http://localhost:3000
   BACKEND_API_URL=http://localhost:8000
   DATABASE_URL=postgresql://username:password@localhost:5432/dbname
   BACKEND_CORS_ORIGINS=http://localhost:3000,http://localhost:8080
   ```

5. **Database Setup**
   ```bash
   # Initialize Alembic (already done)
   alembic init app/alembic
   
   # Create and run migrations
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

6. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## 📁 Project Structure

```
backend/
├── 📄 alembic.ini              # Alembic configuration
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md               # Project documentation
│
├── 📁 app/                    # Main application package
│   ├── 📄 __init__.py         # Package initializer
│   ├── 📄 main.py             # FastAPI application entry point
│   │
│   ├── 📁 alembic/            # Database migrations
│   │   ├── 📄 env.py          # Alembic environment configuration
│   │   ├── 📄 README          # Migration instructions
│   │   └── 📄 script.py.mako  # Migration template
│   │
│   ├── 📁 api/                # API layer
│   │   ├── 📄 __init__.py
│   │   └── 📁 routes/         # API route definitions
│   │       └── 📄 __init__.py
│   │
│   ├── 📁 core/               # Core functionality
│   │   ├── 📄 __init__.py
│   │   └── 📄 config.py       # Application configuration
│   │
│   ├── 📁 crud/               # Database operations (Create, Read, Update, Delete)
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 db/                 # Database configuration
│   │   ├── 📄 __init__.py
│   │   └── 📄 session.py      # Database session management
│   │
│   ├── 📁 middleware/         # Custom middleware
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 models/             # SQLModel database models
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 schemas/            # Pydantic schemas for request/response
│   │   └── 📄 __init__.py
│   │
│   ├── 📁 services/           # Business logic layer
│   │   └── 📄 __init__.py
│   │
│   └── 📁 utils/              # Utility functions
│       └── 📄 __init__.py
```

## 🏗️ Architecture Overview

This template follows a **layered architecture** pattern:

### 📋 Layer Responsibilities

| Layer | Purpose | Examples |
|-------|---------|----------|
| **API** | HTTP endpoints and request handling | Route definitions, request validation |
| **Services** | Business logic and orchestration | User management, data processing |
| **CRUD** | Data access operations | Database queries, data manipulation |
| **Models** | Data structure definitions | SQLModel classes, database tables |
| **Schemas** | Data validation and serialization | Pydantic models for API contracts |

### 🔄 Request Flow

```
🌐 Client Request
    ↓
📡 API Routes (FastAPI)
    ↓
🔧 Services (Business Logic)
    ↓
💾 CRUD Operations
    ↓
🗄️ Database (PostgreSQL)
```

## 📚 Usage Examples

### Adding a New Model

1. **Create the model** (`app/models/user.py`):
   ```python
   from sqlmodel import SQLModel, Field
   from typing import Optional

   class User(SQLModel, table=True):
       id: Optional[int] = Field(default=None, primary_key=True)
       name: str
       email: str = Field(unique=True)
   ```

2. **Create schemas** (`app/schemas/user.py`):
   ```python
   from pydantic import BaseModel

   class UserCreate(BaseModel):
       name: str
       email: str

   class UserResponse(BaseModel):
       id: int
       name: str
       email: str
   ```

3. **Add CRUD operations** (`app/crud/user.py`):
   ```python
   from sqlmodel import Session, select
   from app.models.user import User

   def create_user(session: Session, user_data: dict):
       user = User(**user_data)
       session.add(user)
       session.commit()
       session.refresh(user)
       return user
   ```

4. **Create API routes** (`app/api/routes/users.py`):
   ```python
   from fastapi import APIRouter, Depends
   from sqlmodel import Session
   from app.db.session import get_session

   router = APIRouter(prefix="/users", tags=["users"])

   @router.post("/")
   def create_user(user: UserCreate, session: Session = Depends(get_session)):
       return create_user(session, user.dict())
   ```

## 🔧 Configuration

The application uses **Pydantic Settings** for configuration management. All settings are defined in `app/core/config.py` and can be overridden using environment variables.

### Key Settings

- `FRONTEND_URL`: Frontend application URL
- `BACKEND_API_URL`: Backend API URL
- `DATABASE_URL`: PostgreSQL connection string
- `BACKEND_CORS_ORIGINS`: Allowed CORS origins

## 📊 Database Migrations

This template uses **Alembic** for database migrations:

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---

**Happy coding! 🎉**