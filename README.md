# 📄 Task API – PostgreSQL with Docker & PDF Report Generation

## 📌 Description

This project is a **FastAPI CRUD Task API** that uses **PostgreSQL** as its database. PostgreSQL runs inside **Docker**, and the application connects using environment variables.

The project also includes **PDF report generation** using **ReportLab**. Reports are generated in the background using FastAPI's `BackgroundTasks` and saved in the `reports/` folder.

---

## 🚀 Features

- ✅ Create tasks
- ✅ Read all tasks
- ✅ Read a task by ID
- ✅ Update tasks
- ✅ Delete tasks
- ✅ PostgreSQL database integration
- ✅ Docker & Docker Compose support
- ✅ PDF report generation
- ✅ Background task processing

---

## 🛠️ Technologies Used

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- psycopg
- ReportLab
- python-dotenv

---

## 📁 Project Structure

```text
flyRank-assignment-2/
│
├── reports/
│   └── report_YYYYMMDD_HHMMSS.pdf
│
├── main.py
├── pdf_generator.py
├── repository.py
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/minahilsaghir07-beep/flyRank-assignment-2.git
cd flyRank-assignment-2
```

### 2. Create a `.env` file

Create a `.env` file using `.env.example`.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/tasks
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=tasks
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn psycopg python-dotenv reportlab
```

### 4. Start PostgreSQL

```bash
docker compose up
```

### 5. Run the FastAPI Application

```bash
uvicorn main:app --reload
```

### 6. Open Swagger UI

Open your browser and visit:

```text
http://127.0.0.1:8000/docs
```

---

## 📚 API Endpoints

### Task Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check API status |

### Report Generation

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/reports` | Generate a PDF report in the background |

---

## 📄 PDF Report Generation

The generated PDF report includes:

- Report title
- Date and time of generation
- Task information
- Task status (Done / Pending)

Reports are automatically saved in the **`reports/`** folder.

Example:

```text
reports/report_20260805_231537.pdf
```

---

## 💾 Data Persistence

Data persistence was verified by:

1. Creating tasks through the API.
2. Restarting the PostgreSQL Docker container.
3. Running `GET /tasks`.
4. Confirming that previously created tasks remained available.

---

## ▶️ How to Generate a Report

1. Start PostgreSQL:

```bash
docker compose up
```

2. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

3. Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

4. Execute the following endpoint:

```text
POST /reports
```

5. A PDF report will be generated in the `reports/` folder.

---

## 👩‍💻 Author

**Minahil Saghir**

---

## 📌 Assignment

**FlyRank Backend Assignment – PostgreSQL, Docker & PDF Report Generation**