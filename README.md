# LPU Campus Management System

Modern Django-based campus management project that combines:

- Face-based attendance tracking  
- Makeup/remedial class management  
- Food ordering and peak-time analytics  
- Classroom and resource utilization dashboards

This repository is ready to be pushed to GitHub as a full-stack Django project.

---

## Features

- **Attendance**
  - Face-recognition based attendance using the system camera
  - Daily dashboard for faculty and admins
  - Absentee list and admin tools for resetting and reviewing attendance

- **Makeup / Remedial Classes**
  - Faculty creates makeup classes with a unique remedial code
  - Students enter a 6-digit code to mark attendance
  - Makeup dashboard showing present vs absent students per class
  - Overall attendance rate across all remedial sessions

- **Food Services**
  - Menu display and ordering flow
  - Peak‑time demand analytics by time slot
  - Simple dashboards for canteen staff

- **Resources**
  - Blocks, classrooms, and courses
  - Utilization and faculty workload dashboard
  - Visual gauges and filters for quick admin insight

- **Admin**
  - Django admin configured for all key models  
  - Custom management commands (for example, bootstrapping an admin account)

---

## Tech Stack

- **Backend:** Django (5.x), Python (3.10+)
- **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)
- **Frontend:** Bootstrap 5, Bootstrap Icons, custom CSS
- **Face Recognition / Imaging:** OpenCV, face-recognition, Pillow
- **Config:** Environment variables via `.env` (see `lpu_campus/settings.py`)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>/ERP/lpu_campus
```

If you are already inside this folder locally, you can just initialize Git and add a remote:

```bash
git init
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
```

### 2. Create and activate a virtual environment

On Windows (PowerShell):

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

Install the core Python packages used by this project:

```bash
pip install django python-decouple pillow opencv-python face-recognition
```

If you later add a `requirements.txt`, you can switch to:

```bash
pip install -r requirements.txt
```

### 4. Environment configuration

Create a `.env` file in the project root (`ERP/lpu_campus/`) and set at least:

```env
DEBUG=True
SECRET_KEY=change-me-in-production
ALLOWED_HOSTS=127.0.0.1,localhost
```

You can check `lpu_campus/settings.py` for any additional configuration options (database, media, face-recognition thresholds, etc.).

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create an admin user

There are two options:

- **Standard Django superuser**

  ```bash
  python manage.py createsuperuser
  ```

- **Custom bootstrap command** (if configured)

  ```bash
  python manage.py bootstrap_admin
  ```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the app in your browser:

- Main attendance dashboard: `http://127.0.0.1:8000/attendance/`
- Makeup classes: `http://127.0.0.1:8000/makeup/`
- Food services: `http://127.0.0.1:8000/food/`
- Resources dashboard: `http://127.0.0.1:8000/resources/`
- Django admin: `http://127.0.0.1:8000/admin/`

---

## App Overview

- **accounts**
  - Student model and related authentication/identity data
  - Management command(s) for bootstrapping an admin user

- **attendance**
  - Core webcam-based attendance logic
  - Daily attendance dashboard and absentee list
  - Admin tools (resetting today’s statuses, viewing summaries)

- **makeup**
  - Makeup class model and remedial attendance
  - Student code entry page for remedial sessions
  - Faculty dashboard summarizing present/absent students

- **food**
  - Food items and ordering
  - Peak-time charts/dashboards for demand analysis

- **resources**
  - Blocks, classrooms, and courses
  - Utilization and faculty workload dashboard

---

## Face Attendance Notes

- Uses a webcam to capture frames from the client machine where the server runs.
- Compares live encodings with student face encodings stored in the database.
- Matching thresholds and stability settings can be tuned via Django settings and/or environment variables.

If you deploy this beyond a local machine, ensure you understand the privacy and security implications of storing face images and encodings.

---

## Running Tests

If you add tests to each app, you can run them with:

```bash
python manage.py test
```

---

## Deployment Notes

- Set `DEBUG=False` and configure `ALLOWED_HOSTS` correctly.
- Use a production-ready database (e.g. PostgreSQL).
- Configure a proper web server (e.g. Gunicorn + Nginx) instead of Django’s dev server.
- Make sure environment variables (including `SECRET_KEY`) are set securely and not committed.

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

